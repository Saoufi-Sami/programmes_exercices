# LES COLLECTIONS
# Exercice "Nombre total de caracteres"

#         0         1        2          3         4      5
noms = ["Jean", "Sophie","Martin","Christophe","Zoe","Martin"]


# compter tout les caracteres ex jean 4 + sophie = 10 ..
# premier methode boucle for + len

total = 0

for nom in noms:
    nombre = len(nom)
    total += nombre

print(total)