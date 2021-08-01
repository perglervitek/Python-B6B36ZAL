import string

def decrypt(chiffretext, key):
    allChars = string.ascii_lowercase
    decryptedMessage = ""
    for letter in chiffretext:
        letterIndex = allChars.find(letter)
        movedIndex = letterIndex - key
        movedIndex = movedIndex % len(allChars)
        decryptedMessage += allChars[movedIndex]
    return decryptedMessage

def encrypt(plaintext, key):
    allChars = string.ascii_lowercase
    encryptedMessage = ""
    for letter in plaintext:
        letterIndex = allChars.find(letter)
        movedIndex = letterIndex + key
        movedIndex = movedIndex % len(allChars)
        encryptedMessage += allChars[movedIndex]
    return encryptedMessage


operace = input("(S)ifrovat nebo (D)esifrovat? ")
text = input('Text (malá písmena bez diakritiky): ')
klic = int(input('Klíč: '))
if(operace == "S"):    
    print('Výstup', encrypt(text, klic))
elif(operace == "D"):
    print('Výstup:', decrypt(text, klic))