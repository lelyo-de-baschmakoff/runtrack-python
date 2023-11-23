def echanger_premiere_derniere(liste):
    if len(liste) >= 1:
        liste[0], liste[-1] = liste[-1], liste[0]
    return liste

ma_liste = [1, 2, 3, 4, 5]
print(ma_liste)

ma_liste = echanger_premiere_derniere(ma_liste)
print(ma_liste)
