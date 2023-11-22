def verifier_pair_impair(nombre):
    if isinstance(nombre, int) and nombre >= 0:
        if nombre % 2 == 0:
            print(f"Le nombre {nombre} est pair.")
        else:
            print(f"Le nombre {nombre} est impair.")
    else:
        print("Veuillez entrer un nombre entier positif.")

verifier_pair_impair(5)
verifier_pair_impair(10)
verifier_pair_impair(27)
verifier_pair_impair(-3)
verifier_pair_impair(3.5)
