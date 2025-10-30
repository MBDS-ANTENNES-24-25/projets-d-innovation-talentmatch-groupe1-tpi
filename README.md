# TalentMatch

1.  **Créer un environnement virtuel Django :**
  ```bash
    python -m venv env
    ```
2.  **Activer le environnement virtuel Django :**
    ```bash
    env\Scripts\activate
    ```
3.  **Installer dépendances si ce n'est pas encore fait :**
    ```bash
    pip install -r  requirements.txt
    ```
    ## Si vous avez de nouvelles dépendances,ajouter dans requirements.txt manuellement !!!
4.  **Installer dépendances si ce n'est pas encore fait :**
    Créer un .env et suiver l'exemple dans .env.example
5.  ## Lancer le serveur de développement

    Pour exécuter le serveur de développement Django, ouvrez votre terminal dans le répertoire racine du projet (celui qui contient le fichier `manage.py`) et exécutez la commande suivante :

    ```bash
    uvicorn main:app  --port 8001

    Demarage sans devoir a redemareer a chaque modif 

    uvicorn main:app --reload --port 8001

    ```

  ## desactiver l'environement python
    ```
    env\Scripts\deactivate
    ```
      ## Pour plus de tutoriel sur FastAPI et sa structure clicker sur le lien si dessous
  ⚡**N'effacez aucun __init__.py**

   https://fastapi.tiangolo.com/