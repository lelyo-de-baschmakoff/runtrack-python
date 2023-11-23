def my_long_word(chiffre, chaine):
    mots_long = []
    mot_en_cours = ''
    for caractere in chaine:
        if caractere != ' ':
            mot_en_cours += caractere
        else:
            longueur_mot = 0
            for _ in mot_en_cours:
                longueur_mot += 1
            if longueur_mot > chiffre:
                mots_long.append(mot_en_cours)
            mot_en_cours = ''

        longueur_dernier_mot = 0
    for _ in mot_en_cours:
        longueur_dernier_mot += 1
    if longueur_dernier_mot > chiffre:
        mots_long.append(mot_en_cours)
    
    return mots_long

longueur_minimale = 5
phrase = "La vie est belle quand on la regarde avec des yeux pleins d'émerveillement."

resultat = my_long_word(longueur_minimale, phrase)
print("Mots plus longs que la longueur renseigner:", resultat)
