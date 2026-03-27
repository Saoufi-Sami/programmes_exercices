
def afficher(collection):
    print(f"---- LISTE DES PIZZAS ({len(collection)}) ----")
    for i in collection:
        print(i)


pizzas = ("4 fromages", "végétarienne", "hawai", "calzone")

afficher(pizzas)