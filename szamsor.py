szamok = []
szamsor = True
hossz = int(input("Hány számjegyet adsz meg?: "))

for i in range(1, hossz + 1):
    szamok.append(int(input(f"{i}. szám: ")))

print(f"Számok: {szamok}")


def szamsor_e(x):
    global szamsor
    probak = 1
    kulonbseg = x[probak] - x[0]
    while probak != hossz:
        if kulonbseg == x[probak + 1] - x[probak]:
            probak += 1
        else:
            szamsor = False
            break
        
        szamsor = True
        return probak 

szamsor_e(szamok)

if szamsor == True:
    print("Számsor!")
else:
    print("Nem számsor!")