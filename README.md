# Lancer le projet FastAPI

Pour lancer le projet FastAPI, suivez les étapes ci-dessous :

1. **Cloner le dépôt** :
    ```bash
    git clone <URL_DU_DEPOT>
    cd <NOM_DU_DEPOT>
    ```

2. **Créer un environnement virtuel** :
    ```bash
    python -m venv env
    source env/bin/activate  # Sur Windows, utilisez `env\Scripts\activate`
    ```

3. **Installer les dépendances** :
    ```bash
    pip install -r requirements.txt
    ```

4. **Lancer l'application** :
    ```bash
    python back/app.py
    ```

5. **Accéder à l'application** :
    Ouvrez votre navigateur et allez à l'adresse [http://127.0.0.1:8000](http://127.0.0.1:8000)

6. **Documentation interactive** :
    Vous pouvez accéder à la documentation interactive de l'API à l'adresse [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

Suivez ces étapes pour démarrer et tester votre projet FastAPI localement.


## Description du projet

Il s'agit d'un modèle de machine learning qui permet de détecter les situations de danger des techniciens en fonction des EPI qu'ils ont porté. Ce projet utilise FastAPI pour créer une API permettant d'interagir avec le modèle de machine learning et de prédire les risques potentiels basés sur les équipements de protection individuelle (EPI) des techniciens.

Le modèle a été entraîné à partir de l'algorithme de RandomForest. Voici les résultats obtenus :

**Accuracy**: 0.9620253164556962

|              | precision | recall | f1-score | support |
|--------------|------------|--------|----------|---------|
| **0**        | 1.00       | 0.95   | 0.98     | 66      |
| **1**        | 0.81       | 1.00   | 0.90     | 13      |
| **accuracy** |            |        | 0.96     | 79      |

Ces résultats montrent que le modèle est très performant pour détecter les situations de danger, avec une précision globale de 96%. La classe majoritaire (0) a une précision de 100%, tandis que la classe minoritaire (1) a une précision de 81%, ce qui est acceptable compte tenu du déséquilibre des classes.