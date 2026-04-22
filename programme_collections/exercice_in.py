# LES COLLECTIONS : LISTES / TUPLES
# Exercice "in insensible a la casse"

# premier façon d'ecrire
'''def element_dans_liste(e, l):
    for i in l:
        if e.lower() == i.lower():
            return True
    return False'''
# On parcourt chaque élément de la liste `l`.
# Pour chaque élément, on le compare avec `e` en les mettant tous les deux en minuscules (grâce à lower())
# afin d’ignorer les différences entre majuscules et minuscules.
# Si on trouve une correspondance, on arrête la fonction et on retourne True.
# Si la boucle se termine sans trouver de correspondance, on retourne False (l’élément n’est pas dans la liste).

# deuxieme façon d'ecrire
'''def element_dans_liste(e, l):
    return any(e.lower() == i.lower() for i in l)'''
# any(e.lower() == i.lower() for i in l)
# → On parcourt la liste l, et pour chaque élément i,
#   on compare e et i en minuscules pour ignorer la casse ( c'est la condition ).
# → Si au moins un élément correspond, any() renvoie True,
#   sinon il renvoie False.

# troisieme façon
def element_dans_liste(e, l):
    l_lower = [el.lower() for el in l]
    return e.lower() in l_lower
# On crée une nouvelle liste `l_lower` :
# → on parcourt la liste `l`
# → pour chaque élément `el`, on le met en minuscule avec lower()
# → on obtient donc une liste avec tous les éléments en minuscules
# Ensuite, on compare :
# → e en minuscule
# → avec la liste `l_lower`
# Si e (en minuscule) est dans la liste, on retourne True
# sinon, on retourne False







#         0         1        2            3         4       5
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]

if element_dans_liste("JeAn", noms):
    print("Jean is here")
else:
    print("Jean is not here")