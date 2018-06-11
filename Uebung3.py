import random
zahlen = []
for i in range (0,10):
    wurf = random.randint(1,6)
    zahlen.append(wurf)
    print(wurf, end="...")

print()
print("Ergebnis: ")
print(zahlen)


for i in range(1,7):
    print(i,"er : ", zahlen.count(i))



print("1er:", zahlen.count(1))
print("2er:", zahlen.count(2))
print("3er:", zahlen.count(3))
print("4er:", zahlen.count(4))
print("5er:", zahlen.count(5))
print("6er:", zahlen.count(6))