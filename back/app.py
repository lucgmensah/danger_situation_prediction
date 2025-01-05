from fastapi import FastAPI
import numpy as np
import pandas as pd
import uvicorn

from model import perform_predict

path_model = 'back/model.pkl'
app = FastAPI()


@app.get("/")
def root():
    data = {
        'Scenario': 2,
        'Correct': 0,
        'casque': 0,
        'visiere': 0,
        'col': 0,
        'gant_gauche': 0,
        'gant_droit': 0,
        'veste': 1,
        'Duree': 15
    }

    # Effectuer la prédiction
    dataframe = pd.DataFrame([data])  # Conversion en DataFrame
    prediction = perform_predict(dataframe, path_model)

    # Convertir la prédiction en types natifs Python si nécessaire
    if isinstance(prediction, (np.ndarray, list)):
        prediction = prediction.tolist()  # Convertir les tableaux NumPy ou listes

    elif isinstance(prediction, np.generic):  # Pour des types scalaires NumPy
        prediction = prediction.item()

    # Préparer une réponse sérialisable
    response = {
        "message": f"Hello World. \n L'etat des EPI est : {data}",
        "prediction": prediction
    }

    return response



if __name__ == '__main__':
    uvicorn.run("app:app", host="0.0.0.0",
                port=8000, reload=True)