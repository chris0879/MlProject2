import argparse
import pandas as pd
import mlflow
import os

""" file_path = "/app/mlprojects/dataset.csv"

if os.path.exists(file_path):
    print("Il file esiste.")
else:
    print("Il file non esiste.") """

def load_dataset(dataset_file):
    df = pd.read_csv(dataset_file)
    # Esegui la pre-elaborazione o altre operazioni sul dataset
    return df

def train_model(dataset):
    # Codice per addestrare il modello utilizzando il dataset fornito
    # Restituisci il modello addestrato
    pass

def evaluate_model(model, test_dataset):
    # Codice per valutare il modello utilizzando un dataset di test
    # Restituisci le metriche di valutazione
    pass

def print_evaluation_results(evaluation_results):
    # Stampa i risultati della valutazione
    print("Risultati della valutazione:")
    print(evaluation_results)

def main():
    parser = argparse.ArgumentParser(description='Esempio di script per il progetto di machine learning')
    parser.add_argument('--dataset', type=str, required=True, help='Percorso del file del dataset')

    args = parser.parse_args()

    # Carica il dataset
    dataset = load_dataset(args.dataset)

    # Addestra il modello
    model = train_model(dataset)

    # Valuta il modello
    evaluation_results = evaluate_model(model, dataset)

    # Stampa i risultati della valutazione
    print_evaluation_results(evaluation_results)

    # Registra il modello in MLflow
    with mlflow.start_run():
        mlflow.log_params(vars(args))
        mlflow.sklearn.log_model(model, "model")

if __name__ == '__main__':
    main()
