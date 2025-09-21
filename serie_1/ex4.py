n = int(input("Time is secondes:\n"))
h = n // 3600
mn = (n % 3600) // 60
sec = n % 60

print(f"{h}h{mn}min{sec}sec")