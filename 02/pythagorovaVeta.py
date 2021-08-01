from math import sqrt
def vypocetPrepony(odvesnaA, odvesnaB):
    return sqrt(odvesnaA**2 + odvesnaB**2)

odvesnaA = float(input("Zadej délku jedné odvěsny: "))
odvesnaB = float(input("Zadej délku druhé odvěsny: "))

print(vypocetPrepony(odvesnaA, odvesnaB))