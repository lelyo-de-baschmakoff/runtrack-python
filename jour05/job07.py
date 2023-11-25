def arrondir_notes(liste_notes):
    notes_arrondies = []
    for note in liste_notes:
        if note < 40:
            notes_arrondies.append(note)
        else:
            difference = note % 5
            if difference >= 3:

                note_arrondie = note + (5 - difference)
            else:
                note_arrondie = note
            notes_arrondies.append(note_arrondie)
    return notes_arrondies

liste_de_notes = [58, 83, 73, 18, 23, 48]
notes_arrondies = arrondir_notes(liste_de_notes)
print(notes_arrondies)