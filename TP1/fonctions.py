# Fichier : fonctions.py

def puissance(a, b):
    # Vérification des types
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Only integers are allowed")

    # Cas limite 0^x
    if a == 0:
        if b < 0:
            raise ValueError("0 elevated to a negative power is undefined")
        return 0

    # Cas exposant nul : x^0 = 1
    if b == 0:
        return 1

    # Calcul du produit avec une boucle for
    resultat = 1
    for _ in range(abs(b)):
        resultat *= a

    # Si l'exposant est négatif : a^(-b) = 1 / (a^b)
    if b < 0:
        return 1 / resultat

    return resultat

    
