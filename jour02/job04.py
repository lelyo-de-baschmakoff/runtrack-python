while True:
    try:
        N = int(input("Entrez un entier supérieur à zéro : "))
        if N <= 0:
            print("Veuillez entrer un entier supérieur à zéro.")
        else:
            break
    except ValueError:
        print("Veuillez entrer un nombre entier.")

print(f"Tables de multiplication de 1 à {N}:")
for i in range(1, N + 1):
    print(f"Table de multiplication de {i}:")
    for j in range(1, 11):
        result = i * j
        print(f"{i} x {j} = {result}")
    print()  # Ajoute une ligne vide entre les tables
