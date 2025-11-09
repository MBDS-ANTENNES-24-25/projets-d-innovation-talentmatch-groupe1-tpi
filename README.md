
# Fonctionnalité : Matching CV → Offres

## 1. Vue côté utilisateur

Les utilisateurs peuvent accéder à une fonctionnalité permettant de trouver des offres correspondant à leur profil.  
Deux options s’offrent à eux :

1. **Remplir manuellement un formulaire** contenant les informations principales de leur CV (informations personnelles, expériences, formations, compétences, etc.)  
2. **Uploader leur CV** au format **PDF** ou **DOCX**. Dans ce cas, le système extrait automatiquement les informations du document et **pré-remplit le formulaire**.

Une fois le formulaire vérifié et envoyé, le système **analyse le profil de l’utilisateur** et **affiche une liste d’offres correspondantes**, triées par **pertinence**.

---

## 2. Fonctionnement côté interne

Lorsqu’un utilisateur choisit d’uploader un fichier **PDF** ou **DOCX** de son CV :

1. Une **API d’extraction de texte** transforme le document en texte brut.  
2. Ce texte est ensuite envoyé à un **modèle LLM (Gemini)**, qui le convertit en une **structure JSON normalisée** correspondant au schéma `Candidat`.  
3. La structure générée est **validée** via un modèle **Pydantic** pour garantir la cohérence et le bon typage des données.  
4. Une fois la structure validée, un **API de matching** est appelée.  
   Cet API compare les informations du candidat (compétences, expériences, secteur d’activité, etc.) avec les offres disponibles.  
5. Le résultat renvoyé est une **liste d’offres triées** selon un **score de similarité**, du plus pertinent au moins pertinent.  

Le score de pertinence est calculé à partir des vecteurs d’embedding du candidat et des offres, permettant une **recommandation intelligente** et personnalisée.

---

## 3. Résultat final

L’utilisateur obtient une **liste d’offres classées par compatibilité**, avec la possibilité d’examiner chaque offre, avec lien pour postuler.



# Déploiement du Frontend et du Backend

Cette section décrit le processus complet de **déploiement continu ** mis en place pour les deux composants principaux du projet **TalentMatch** :
- Le **frontend** (interface web utilisateur React) hébergé sur **Render.com**
- Le **backend** (API FastAPI) déployé via **Google Cloud Run**

---

## 1. Structure du projet et objectifs

Le projet est organisé sous forme de **monorepo** avec la structure suivante :

```
Talentmatch-monorepo/
├── TalentMatch/          # Backend (FastAPI)
├── Frontend/             # Frontend (React)
├── .github/workflows/    # Fichiers GitHub Actions
└── docker-compose.yml    # Configuration locale de développement
```

L’objectif du pipeline CI/CD est de :
- Automatiser le **build et le push** des images Docker vers **Docker Hub**
- Déployer automatiquement chaque service (front et back) dans son environnement cloud respectif après chaque mise à jour du code.

---

## 2. Pipeline CI/CD – GitHub Actions

Le déploiement repose sur **GitHub Actions**, un système d’automatisation intégré à GitHub.  
Chaque fois qu’un **push** ou un **merge sur la branche principale (main)** est effectué, un workflow est déclenché pour :
1. Construire les images Docker
2. Publier ces images sur **Docker Hub**
3. Déclencher le déploiement sur **Render.com** (frontend) et **Google Cloud Run** (backend)

Deux workflows principaux assurent cette automatisation :
- `sync-modules.yml` : permet la **détection des modifications** dans les branches principales du monorepo.
- `ci-cd.yml` : gère le **build** et le **push** des images Docker pour le frontend et le backend.

---

## 3. Déploiement du Frontend – Render.com

Le **frontend** est déployé sur la plateforme **Render.com**, qui simplifie le déploiement continu pour les applications web.

1. L’image Docker du frontend (kaloina/front-talentmatch:latest) est automatiquement poussée sur Docker Hub via GitHub Actions.
2. Après le push de l’image, un webhook est déclenché pour redéployer automatiquement la nouvelle version sur Render.
3. Le site est ensuite accessible via une URL publique Render (ex. https://front-talentmatch.onrender.com/).

---

## 4. Déploiement du Backend – Google Cloud Run

Le **backend FastAPI** est conteneurisé dans Docker et déployé sur **Google Cloud Run**, un service serverless qui exécute automatiquement les conteneurs.

L’image Docker du backend (`kaloina/back-talentmatch:latest`) est poussée sur **Docker Hub** via GitHub Actions.  
Cloud Run récupère ensuite cette image et la déploie automatiquement dans son environnement, assurant :
- le scaling automatique (1 à 3 instances),
- la gestion des variables d’environnement,
- la sécurité et la supervision.

Le backend est accessible via une URL sécurisée :
```
https://back-talentmatch-2-596715584253.us-central1.run.app/
```


---

