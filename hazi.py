#szám kitalálós játék
import random

print("Gondoaltam egy számra 0 és 100 között találd ki!")

number = random.randint(0, 100)
inputNumber = None
probak = 1

def checkNumber(szam):
    global number
    global probak

    if szam >= 0 and szam <= 100:
        if szam < number:
            print("Túl kicsi!")
            probak += 1
        elif szam > number:
            print("Túl nagy!")
            probak += 1
    else:
        print("A szám legyen 0 és 100 között!!")
    
    return probak

while inputNumber != number:
    inputNumber = int(input(""))
    checkNumber(inputNumber)


print("ELTALÁLTAD A SZÁMOT!!!!!!")
print(f"A szám ez volt: {number}")
print(f"Ennyi próbálkozásból: {probak}")