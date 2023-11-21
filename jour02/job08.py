a = float(input("Saisissez la longueur du côté a : "))
b = float(input("Saisissez la longueur du côté b : "))
c = float(input("Saisissez la longueur du côté c : "))

if a + b > c and a + c > b and b + c > a:
    print("Ces longueurs peuvent former un triangle.")
    
    if a == b == c:
        print("Il s'agit d'un triangle équilatéral.")
    elif a == b or a == c or b == c:
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            print("Il s'agit d'un triangle rectangle isocèle.")
        else:
            print("Il s'agit d'un triangle isocèle.")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Il s'agit d'un triangle rectangle.")
    else:
        print("Il s'agit d'un triangle quelconque.")
else:
    print("Ces longueurs ne peuvent pas former un triangle.")