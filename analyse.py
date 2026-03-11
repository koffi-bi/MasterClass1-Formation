def analyse_donnees(df):

    print("Statistiques générales")
    print(df.describe())

    print("\nComics par pays")
    print(df["Country of Origin"].value_counts())