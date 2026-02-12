# EXERCICES FONTCIONS
# Tables de multiplication
#
#
#1 x 4 = 4
#2 x 4 = 8
#3 x 4 = 12
# ...
#10 x 4 = 40
#
#afficher_table_multiplication(n)
#min/max
# erreur : si min > max

def afficher_table_multiplication(numero: int,valeur_min: int,valeur_max: int):
    if valeur_min > valeur_max:
        print("Erreur")
        return False

    for i in range(valeur_min,valeur_max+1):
        print(f"{numero} x {i} = {numero*i}")
    return True




afficher_table_multiplication(6,9,10)