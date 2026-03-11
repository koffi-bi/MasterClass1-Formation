from collecte import charger_donnees
from nettoyage import nettoyer_donnees
from visualisation import plot_ratings  # importer la fonction

from analyse import analyse_donnees

df = charger_donnees()

df = nettoyer_donnees(df)

analyse_donnees(df)
plot_ratings(df) #Permet la visualisation