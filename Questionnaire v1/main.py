# LES FONCTIONS : PROJET QUESTIONNAIRE
#
# Question : Quelle est la capitale de la france ?
# (a) Marseille
# (b) Nice
# (c) Paris
# (d) Nantes
#
# Votre réponse :
# Bonne réponse / Mauvaise réponse

# ...
# Question : Quelle est la capitale de l'Italie ?
#...
#
# 4 questions


def question(pays,choix1,choix2,choix3,choix4,bonne_reponse):
    print(f"Quelle est la capitale du pays : {pays} ?\n"
          f"(a) {choix1} \n"
          f"(b) {choix2} \n"
          f"(c) {choix3} \n"
          f"(d) {choix4} \n")
    reponse = input("Votre réponse : ")
    if reponse == bonne_reponse:
        print("Bonne réponse")
    else:
        print("Mauvaise réponse")

nb_questions = 4

questions = [
    ("Maroc", "Rabat", "Meknes", "Tanger", "Fes", "a"),
    ("Italie", "Rome", "Milan", "Naples", "Turin", "a"),
    ("France", "Paris", "Lyon", "Marseille", "Nice", "a"),
    ("Espagne", "Madrid", "Barcelone", "Valence", "Séville", "a")
]
for i in range(nb_questions):
    question(*questions[i])


# Un tuple est une structure de données en Python qui permet de stocker
# plusieurs valeurs ensemble (comme une liste), mais qui ne peut pas être modifiée.
# On le reconnaît aux parenthèses : ( ... )
#
# Exemple :
# ("Maroc", "Rabat", "Meknes", "Tanger", "Fes", "a")
#
# Ici ce tuple contient toutes les informations pour une question :
# pays, choix1, choix2, choix3, choix4 et la bonne réponse.
#
# L'étoile (*) sert à "décompresser" ce tuple.
# Sans l'étoile, Python enverrait le tuple entier comme un seul paramètre
# à la fonction question(), ce qui provoquerait une erreur car la fonction
# attend 6 paramètres séparés.
#
# Avec *, Python transforme automatiquement :
# ("Maroc", "Rabat", "Meknes", "Tanger", "Fes", "a")
#
# en :
# question("Maroc", "Rabat", "Meknes", "Tanger", "Fes", "a")
