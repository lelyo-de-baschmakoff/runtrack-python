def est_nombre_premier(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def afficher_nombres_premiers(maximum):
    print("Nombres premiers jusqu'à", maximum, ":")
    for nombre in range(2, maximum + 1):
        if est_nombre_premier(nombre):
            print(nombre, end=" ")

afficher_nombres_premiers(1000)
