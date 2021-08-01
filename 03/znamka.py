znamka = ""
pocet = 0
suma = 0
while znamka != 0:
    znamka = int(input("Zadej"))
    pocet += 1
    suma += znamka
print(suma / pocet - 1)