def triangle(height):
    if height <= 0:
        raise ValueError("Hauteur invalide: La hauteur doit être supérieure à 0")
    
    l_diag = "/" 
    r_diag = "\\" 

    empty_side = height - 1

    empty_mid = height * 2 - empty_side * 2 - 2

    for i in range(height):

        empty_char = " " * empty_side
        empty_char_mid = " " * empty_mid

        if empty_mid == height * 2 - 2:
            empty_char_mid = "_" * empty_mid

        print(f"{empty_char}{l_diag}{empty_char_mid}{r_diag}")

        empty_side -= 1
        empty_mid += 2

try:
    hauteur = int(input("Entrez la hauteur du triangle : "))
    triangle(hauteur)
except ValueError:
    print("Veuillez entrer un nombre entier valide pour la hauteur.")