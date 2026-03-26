# LISTES - ALGO :VALEUR LA PLUS PETITE

# exemple d'application de taxi qui recherche le chauffeur le plus proche


distance_chauffeur_km = [1.5, 2.2, 0.4, 0.9, 7.1, 1.1, 0.6]

distance_min = distance_chauffeur_km[0]
for distance in distance_chauffeur_km:
    if distance < distance_min:
        distance_min = distance

print("Distance minimal:",distance_min)