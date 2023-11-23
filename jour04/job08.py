L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

somme_valeurs_paires = 0

for nombre in L:
    if nombre % 2 == 0: 
        somme_valeurs_paires += nombre

print("La somme des valeurs paires dans la liste est :", somme_valeurs_paires)
