# implémenter la fontcion qui permet de recuperer et afficher

def recuperer_et_afficher_infos_personne(numero_personne):
    nom = input("Nom de la personne  "  + numero_personne + " : ")
    age = input("Age de la personne : " + numero_personne + " : ")
    print("La personne est ",nom, "son age est",age,"ans")
    print("Le nom comporte", len(nom), "lettres")

recuperer_et_afficher_infos_personne(str(1))
recuperer_et_afficher_infos_personne(str(2))
