# Fichier : fonctions.py

def puissance(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Only integers are allowed")
    if a == 0 and b < 0:
        raise ValueError("0 elevated to a negative power is undefined")
    return a ** b

