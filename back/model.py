import os
import pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


# URL du fichier CSV
data_path = 'data/data_technicien.csv'
model_path = 'back/model.pkl'

def data_preparation(url):
    data = pd.read_csv(url)

    # Séparer les données du technicien 1
    data1 = data.drop(columns=['t2_casque', 't2_visiere', 't2_veste', 't2_col']).copy()

    # Renommer les colonnes des données du technicien 1
    data1.rename(
        columns={
            't1_casque': 'casque',
            't1_visiere': 'visiere',
            't1_veste': 'veste',
            't1_col': 'col',
            't1_gant_gauche': 'gant_gauche',
            't1_gant_droit': 'gant_droit'
        },
        inplace=True
    )

    # Séparer les données du technicien 2
    data2 = data[['Scenario', 'Correct', 'Timestamp', 'Datetime', 't2_casque', 't2_visiere', 't2_veste', 't2_col', 'danger']].copy()

    # Renommer les colonnes des données du technicien 2
    data2.rename(
        columns={
            't2_casque': 'casque',
            't2_visiere': 'visiere',
            't2_veste': 'veste',
            't2_col': 'col'
        },
        inplace=True
    )

    data12 = pd.concat([data1.dropna(), data2.dropna()], ignore_index=True)

    # Mettre veste a 1 si col est a 1
    data12['veste'] = data12.apply(lambda row: 1 if row['col'] == 1 else row['veste'], axis=1)
    data12.sort_values(by='Datetime', inplace=True)
    data12.reset_index(drop=True, inplace=True)

    data12

    # Séparer les données en X (features) et y (labels)
    data12 = data12.fillna(0)
    X, y = data12.drop(['danger', 'Datetime'], axis=1), data12['danger']
        
    df = pd.concat([X, y], axis=1)

    # Ensure 'Timestamp' is of datetime dtype
    # df['Timestamp'] = pd.to_datetime(df['Timestamp'])

    # Calculer la différence entre les timestamps pour chaque scénario
    df['Duree'] = df.groupby('Scenario')['Timestamp'].diff().fillna(0).astype(int)

    # Supprimer timestamp
    df = df.drop(columns=['Timestamp'])

    X, y = df.drop(['danger'], axis=1), df['danger']

    return X, y


def train_model(X, y, path_model):

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X , y)

    # save the model
    dir = os.path.dirname(path_model)
    if not os.path.exists(dir):
        os.makedirs(dir)
    with open(path_model, 'wb') as file:
        pickle.dump(model, file)
    
    print('Model is saved in', path_model)


def perform_predict(X: pd.DataFrame, path_model):
    #load the model
    with open(path_model, 'rb') as file:
        model = pickle.load(file)
    
    prediction = model.predict(X)
    
    return prediction[0]


if __name__ == '__main__':
    X, y = data_preparation(data_path)
    model = train_model(X, y, model_path)