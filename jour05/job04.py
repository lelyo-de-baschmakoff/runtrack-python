def diagonal_carpet(n):
    if n <= 0:
        raise ValueError("Taille invalide, doit être au dessus de 0")

    border_line = "-" * (n + 1)

    print(f"+{border_line}+")

    val = n

    for i in range(n + 1):
        left = "#" * val
        right = "#" * (n - val)

        print(f"|{left} {right}|")

        val -= 1

    print(f"+{border_line}+")


diagonal_carpet(10)