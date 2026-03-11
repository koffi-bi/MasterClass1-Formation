import matplotlib.pyplot as plt

def plot_ratings(df):
    df["Rating (out of 10)"].hist()
    plt.title("Distribution des notes des comics")
    plt.xlabel("Rating")  # <-- PAS de texte après le parenthèse
    plt.ylabel("Nombre")
    plt.show()