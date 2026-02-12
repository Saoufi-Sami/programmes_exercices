
def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ? ")
        if reponse_nom == "":
            print("ERREUR : Vous n'avez pas entré de nom")
    return reponse_nom


def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne + " Quel est votre age ? ")
        try:
            age_int = int(age_str)
        except:
            print("ERREUR: Vous devez rentrer un nombre pour l'age")

    return age_int

def afficher_informations_personne(nom, age, taille=0):
    print("Vous vous appelez " + nom + " , vous avez " + str(age) + " ans")
    print("L'an prochain vous aurez " + str(age + 1) + " ans")

    if  age == 17:
        print("vous etes presque Majeur ")
    elif 12 <= age < 18:
        print("vous etes adolescent")
    elif age == 1 or age == 2:
        print("vous etes Bebe")
    elif age == 18:
        print("vous etes tout juste Majeur Felicitation")
    elif age > 60:
        print("Vous etes Senior")
    elif  age > 18:
        print("vous etes Majeur")
    elif age < 10:
        print("Vous etes Enfant")
    else:
        print("vous etes Mineur")


    if not taille ==0:
     print("votre taille est " + str(taille) + " m")





"""

# Demander le nom
nom1 = demander_nom()
nom2 = demander_nom()

# Demander l'age
age1 = demander_age(nom1)
age2 = demander_age(nom2)

# affichage
afficher_informations_personne(nom1, age1)
afficher_informations_personne(nom2, age2)"""




NB_PERSONNES = 1

for i in range(0,NB_PERSONNES):
 nom = "personne" + str(i+1)
 age = demander_age(nom)
 afficher_informations_personne(nom, age, )



