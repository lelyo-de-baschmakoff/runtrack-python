def afficher_produits(type_produit, saison):
    if type_produit == "fruits":
        if saison == "hiver":
            print("Orange, mandarine et kiwi")
        elif saison == "ete":
            print("Poire, fraise, cassis")
    elif type_produit == "legume":
        if saison == "hiver":
            print("Carotte, topinambour, endive")
        elif saison == "ete":
            print("Artichaut, aubergine, navet")
    else:
        print("Type de produit ou saison non reconnu")

afficher_produits("fruits", "hiver")
afficher_produits("fruits", "ete")
afficher_produits("legume", "hiver")
afficher_produits("legume", "ete")
