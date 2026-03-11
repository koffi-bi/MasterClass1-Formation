def nettoyer_donnees(df):

    df = df.drop_duplicates()

    df["Release Year"] = df["Release Year"].astype(int)
    df["Page Count"] = df["Page Count"].astype(int)
    df["Rating (out of 10)"] = df["Rating (out of 10)"].astype(float)

    return df