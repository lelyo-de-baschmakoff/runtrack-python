def tri_a_bulles(liste):
    while True:
        swapped = False
        i = 0
        while True:
            try:
                if liste[i] > liste[i + 1]:
                    liste[i], liste[i + 1] = liste[i + 1], liste[i]
                    swapped = True
                i += 1
            except IndexError:
                break
        if not swapped:
            break

def arrondir_liste(liste):
    arrondi_liste = []
    for nombre in liste:
        arrondi = int(nombre)
        arrondi_liste.append(arrondi)
    return arrondi_liste

liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
liste_arrondie = arrondir_liste(liste)
tri_a_bulles(liste_arrondie)

print(liste_arrondie)
