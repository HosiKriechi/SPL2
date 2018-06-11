
liste = []
eingabe = ""

while(eingabe != "-1"):
    eingabe = input("Bitte eine Zahl eingeben:")
    zahl = int(eingabe)
    liste.append(zahl)
print("ende.")

liste.sort()
print(liste)