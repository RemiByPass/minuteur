import time
print("Codez par rxmii6z#7867")
print("Ajoutez un temps de décompte (en seconde)")
decompte = float(input("Nombres de secondes = "))
time.sleep(1)
print("Un décompte de", decompte, "secondes va ce lancer...")
print("Décompte lancer...")
time.sleep(0.5)
while decompte >= 0:
    print(decompte, "secondes restantes...")
    decompte = decompte - 1
    time.sleep(1)
print("Terminer !")
