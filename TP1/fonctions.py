# Fichier : fonctions.py

def puissance(a, b):
    """
    Calcule a à la puissance b.
    Vérifie que les deux arguments sont des entiers, sinon lève une exception.
    """
    if not type(a) is int:
        raise TypeError("Only integers are allowed")
    if not type(b) is int:
        raise TypeError("Only integers are allowed")
    return a ** b
