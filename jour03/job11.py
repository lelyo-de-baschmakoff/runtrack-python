def time_to_text(minutes):
    if isinstance(minutes, int) and minutes >= 0:
        heures = minutes // 60
        minutes_restantes = minutes % 60

        if heures == 1:
            heures_text = "heure"
        else:
            heures_text = "heures"

        if minutes_restantes == 1:
            minutes_text = "minute"
        else:
            minutes_text = "minutes"

        print(f"{heures} {heures_text} et {minutes_restantes} {minutes_text}")
    else:
        print("Veuillez entrer un nombre entier positif.")

time_to_text(800)
