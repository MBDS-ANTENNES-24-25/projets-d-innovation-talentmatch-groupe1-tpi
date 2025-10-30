from sentence_transformers import SentenceTransformer, util
from services import candidatService
from services import offreService

model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")



async def match_offres_for_cv(cv_id, top_n=None):
    cv_candidat = await candidatService.getCandidatById(cv_id)
    cv_embedding = model.encode(cv_candidat.contenu, convert_to_tensor=True)
    offres = await offreService.getAllOffres()
    offre_texts = [offre.contenu for offre in offres]
    offre_embeddings= model.encode(offre_texts, convert_to_tensor=True)

    """Retourne les offres les plus pertinentes pour un CV donné"""
    scores = util.cos_sim(cv_embedding, offre_embeddings)[0]
    best_idx = scores.argsort(descending=True)

    results = []
    for idx in best_idx:
        score_val = float(scores[idx])
        if score_val != 0:
            offre = offres[idx]
            results.append({
                "offre": offre,
                "score": score_val,
            })
        else:
            break 

    # 5) Limite top_n si demandée
    if top_n is not None:
        return results[:top_n]
    return results




async def match_cvs_for_offre(offre_id, top_n=None):
    offre = await offreService.getOffreById(offre_id)
    cvs = await candidatService.getAllCandidats()

    # Encodage
    offre_embedding = model.encode(offre.contenu, convert_to_tensor=True)
    cv_texts = [cv.contenu for cv in cvs]
    cv_embeddings = model.encode(cv_texts, convert_to_tensor=True)

    # Similarités
    scores = util.cos_sim(offre_embedding, cv_embeddings)[0]

    # Tri décroissant
    best_idx = scores.argsort(descending=True)

    results = []
    for idx in best_idx:
        score_val = float(scores[idx])
        if score_val != 0:  
            candidat = cvs[idx]
            results.append({
                "candidat": candidat,
                "score": score_val,
            })
        else:
            break  

    
    if top_n is not None:
        return results[:top_n]
    return results
