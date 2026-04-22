# LES COLLECTIONS : LISTES / TUPLES
# Exercice "in insensible a la casse"


def element_dans_liste(e, l):
    return e in l




#         0         1        2            3         4       5
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]

if element_dans_liste("JeAn", noms):
    print("Jean est la")
else:
    print("Jean n'est pas là")