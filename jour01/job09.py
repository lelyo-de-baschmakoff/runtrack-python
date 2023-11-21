nom_produit = "Ordinateur portable"
prix_unitaire = 1200
quantite_stock = 50

print(f"Nom du produit : {nom_produit}")
print(f"Prix unitaire : {prix_unitaire} €")
print(f"Quantité en stock : {quantite_stock}")

achat = int(input("Combien d'unités souhaitez-vous acheter ? "))
quantite_stock += achat

prix_unitaire *= 1.1

print("\nAprès l'achat et l'augmentation du prix en raison de l'inflation :")
print(f"Nom du produit : {nom_produit}")
print(f"Nouveau prix unitaire : {prix_unitaire:.2f} €")
print(f"Nouvelle quantité en stock : {quantite_stock}")
