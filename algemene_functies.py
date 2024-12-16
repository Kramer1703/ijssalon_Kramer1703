#Huiswerkopdracht 2
def mijn_functie1(a):   
    uitkomst = a * a
    return uitkomst

kwadraat = mijn_functie1(25)
print(kwadraat)

#Huiswerkopdracht 3
def mijn_functie2(getal1, getal2):
    mijn_lijst = []
    mijn_lijst.append(getal1 + getal2)
    mijn_lijst.append(getal1 - getal2)
    mijn_lijst.append(getal1 * getal2)
    mijn_lijst.append(getal1 / getal2)
    return mijn_lijst

lijst_getallen = mijn_functie2(25, 5)
print(lijst_getallen)