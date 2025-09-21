distance = float(input("Veuillez saisir la distance en (km):\n"))
temps = float(input("Veuillez saisir le temps en minutes\n"))

temps_en_secondes = temps * 60
distance_en_m = distance * 1000
vitesse = distance_en_m / temps_en_secondes

print(f"la vitesse est {vitesse}m/s") 