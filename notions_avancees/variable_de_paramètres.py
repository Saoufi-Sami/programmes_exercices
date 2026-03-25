# PYTHON FONCTIONS : NOTIONS AVANCÉES
#
# Nombre de variable de paramètres

# Premiere methode :
'''def a (age, taille, poids):
    print("toto", age, taille, poids)

a(20,1,65)'''

# Deuxieme methode
'''def somme(*nombres):
    resultat = 0
    for n in nombres:
        resultat += n
    return resultat

print(somme(5,35,6,4,7,5,4))'''

# *nombres permet de passer un nombre variable d’arguments à la fonction
# Tous les arguments sont regroupés automatiquement dans un tuple appelé "nombres"
#
# Exemple :
# somme(5, 35, 6, 4) → nombres = (5, 35, 6, 4)
#
# Ensuite, la boucle "for n in nombres" parcourt chaque élément du tuple
# À chaque tour, "n" prend une valeur du tuple (5 puis 35 puis 6 etc.)
#
# On additionne chaque valeur dans la variable "resultat"
# puis on retourne le total à la fin avec "return resultat"