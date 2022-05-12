import random

kiiras = True

kor = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]    #♡
karo = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]   #♢
treff = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]  #♣
pikk = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]   #♤

def kartya():
    szin = random.randint(1,4)

    match szin:
        case 1:
            card = [random.choice(kor), ]
            kor.remove(card[0])
            card.insert(0, "♡")
        case 2:
            card = [random.choice(karo), ]
            karo.remove(card[0])
            card.insert(0, "♢")
        case 3:
            card = [random.choice(treff), ]
            treff.remove(card[0])
            card.insert(0, "♣")
        case 4:
            card = [random.choice(pikk), ]
            pikk.remove(card[0])
            card.insert(0, "♤")

    return card

def osszeg(x):
    osszesen = x[0][1]

    for i in range(1, len(x)):
        osszesen += x[i][1]

    if kiiras == True:
        print(f"Összegük: {osszesen}")

    return osszesen

playerCard = [kartya(), kartya()]
bankCard = [kartya(), kartya()]

print("Megkapod az első kártád")
print("Az osztó is kap egy kártyát")
print("Megkapod a második kártyád")
print("Az osztó is megkapja a második lapját")
print(f"Kártyáid: {playerCard}")
osszeg(playerCard)
print(f"Az osztó egyik lapja: {bankCard[0]}")

valasz = str(input("Kérsz mégegy kártyát(igen/nem)? "))

while valasz != "nem":
    playerCard.append(kartya())
    print(f"Kártyáid{playerCard}")

    if osszeg(playerCard) > 21:
        playerCard.clear
        playerCard.append([0, 0])
        break
    else:
        valasz = str(input("Kérsz mégegy kártyát(igen/nem)? "))

print(f"Az osztó kártyáti: {bankCard}")

while osszeg(bankCard) <= 16:
    bankCard.append(kartya())
    print(f"Az osztó kártyái a húzás után: {bankCard}")

kiiras = False

if osszeg(bankCard) >21:
    bankCard.clear
    bankCard.append([0, 0])

if osszeg(playerCard) > osszeg(bankCard):
    print("Nyertél!!!")
elif osszeg(bankCard) == osszeg(bankCard):
    print("Döntetlen!")
else:
    print("Vesztettél!")