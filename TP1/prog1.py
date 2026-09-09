# Fichier : prog1.py
import fonctions as f

# Q2.1 : Boucle infinie demandant un nombre et affichant son carré (arrêt avec CTRL-C)
# (Vous pouvez décommenter cette partie pour tester la saisie en boucle normale)
# while True:
#     nombre = int(input("Entrer un nombre : "))
#     print(f"Le carré de {nombre} est : {nombre ** 2}")

# Q2.3 & Q2.5 : Appel de la fonction puissance et test de l'erreur avec des flottants
try:
    # On passe un flottant (2.5) pour vérifier que l'erreur TypeError se déclenche bien (Q2.5)
    a = 2
    b = 3
    
    # Appel de la fonction puissance depuis le module 'fonctions' (Q2.3)
    res = f.puissance(a, b)
    print(f"{a} élevé à la puissance {b} est égal à : {res}")

except TypeError as e:
    # Capture et affichage de l'exception levée par la fonction
    print(f"Erreur interceptée avec succès : {e}")