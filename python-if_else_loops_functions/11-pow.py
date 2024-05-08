#!/usr/bin/python3
def pow(a, b):
    result = 1                   # Étape 1: Initialisation du résultat à 1
    for _ in range(abs(b)):     # Étape 2: Itération à travers la valeur absolue de b
        result *= a             # Étape 3: Calcul de la puissance en multipliant result par a
    if b < 0:                   # Si b est négatif
        return 1 / result       # Étape 4: Si b est négatif, on retourne l'inverse du résultat
    return result

