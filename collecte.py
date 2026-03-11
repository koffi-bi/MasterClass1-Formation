import pandas as pd

def charger_donnees():
    df = pd.read_csv("comic.csv")
    return df