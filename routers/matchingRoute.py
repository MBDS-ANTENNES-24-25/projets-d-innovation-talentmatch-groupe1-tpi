from fastapi import APIRouter
from controllers import matchingController as ctrl 


router = APIRouter(
    prefix="/matching",
    tags=["matching"],
    responses={404: {"description": "Page non trouvée"}}
)


@router.get("/cv/{candidat_id}" )
async def cv_get_offres(candidat_id: str):
    return await ctrl.cvMatchOffres(candidat_id)


@router.get("/offre/{offre_id}")
async def offres_get_candidats(offre_id: str):
    return await ctrl.offreMatchCandidats(offre_id)