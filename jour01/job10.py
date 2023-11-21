montant_initial = 10000
taux_rendement_annuel = 8

gain_annuel = montant_initial * (taux_rendement_annuel / 100)

print(f"Le gain annuel initial est de : {gain_annuel} euros")

montant_initial += 5000
taux_rendement_annuel += 2

nouveau_gain_annuel = montant_initial * (taux_rendement_annuel / 100)

print(f"Avec l'augmentation du capital et du taux, le nouveau gain annuel est de : {nouveau_gain_annuel} euros")

montant_initial *= 0.9
taux_rendement_annuel -= 1

montant_final = montant_initial * (1 + taux_rendement_annuel / 100)

print(f"Après le retrait et la diminution du rendement, le montant final de l'investissement est de : {round(montant_final, 2)} euros")

