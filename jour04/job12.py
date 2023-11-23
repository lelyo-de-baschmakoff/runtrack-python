def tri_croissant(liste):
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

L = [12, 1, 23, 7, 47, 4]
tri_croissant(L)
print(L)