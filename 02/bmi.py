def getBmi(height, weight):
    if height != 0:
        return weight / (height**2)
    else: 
        raise ZeroDivisionError("Výška nesmí být nulová ")
def getWeightGroup(bmi):
    if bmi < 16.5:
        return ("Těžká podvýživa")
    if bmi < 18.5:
        return ("Těžká podvýživa")
    if bmi < 25:
        return ("Ideální váha")
    if bmi < 30:
        return ("Nadváha")
    else:
        return ("Obezita")

hmotnost = float(input("Zadejte hmotnost v kg: "))
vyska = float(input("Zadejte výšku v cm: "))
vyska = vyska / 100
bmi = getBmi(vyska, hmotnost)

print("Hodnota BMI je:", round(bmi, 2))
print(getWeightGroup(bmi))
