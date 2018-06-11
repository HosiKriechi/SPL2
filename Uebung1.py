zahl = input("1.te Zahl eingeben")
zahl2 = input ("2.te Zahl eingeben")
zahl3 = input ("3.te Zahl eingeben")

if( zahl < zahl2 < zahl3 ):
    print(zahl,zahl2,zahl3)

if(zahl2 < zahl3 < zahl):
    print(zahl2,zahl3,zahl1)
 
if(zahl2 < zahl < zahl3):
    print(zahl2,zahl,zahl3)

if(zahl3 < zahl2 < zahl):
    print(zahl3,zahl2,zahl)

if(zahl3 < zahl < zahl2):
    print(zahl3,zahl,zahl2)
    