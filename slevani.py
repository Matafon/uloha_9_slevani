
def slevani(seznam_1, seznam_2):
    vysledek = []
    for i in range(max(len(seznam_1), len(seznam_2))):
        if i < len(seznam_1):
            vysledek.append(seznam_1[i])
        if i < len(seznam_2):
            vysledek.append(seznam_2[i])
    return(vysledek)


seznam_1 = [int(x) for x in input("Zadej číslo: ").split(',')]
seznam_2 = [int(x) for x in input("Zadej číslo: ").split(',')]
print(slevani(seznam_1, seznam_2))