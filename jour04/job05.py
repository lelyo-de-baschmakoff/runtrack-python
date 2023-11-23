L = [1, 2, 3, 4, 5]

print (L)

deuxieme_valeur = L[1]
print(deuxieme_valeur)

def remplacer_valeur(liste):
    liste[3] = liste[2] + liste[4]
    return liste

L = remplacer_valeur(L)
print (L)

derniere_valeur = L[-1]
print(derniere_valeur)
