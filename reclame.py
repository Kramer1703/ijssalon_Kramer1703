from algemene_functies import mijn_functie2
#Huiswerkopdracht 5
def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs * (1 - korting)   
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs:.2f}"
    return uitvoer

ijssmaak = "citroen"
huidige_prijs = 6.75
procentkorting = 0.4
aanbieding_tekst = aanbieding_1(ijssmaak,huidige_prijs,procentkorting)
print(aanbieding_tekst)
#Huiswerkopdracht 6
def inkomsten_totaal(inkomsten): 
    inkomsten_totaal = sum(inkomsten)          
    #for dagen in inkomsten:
        #inkomsten_totaal += dagen
    return inkomsten_totaal
Dagen_week = []
Maandag = 750
Dinsdag = 500
Woensdag = 0
Donderdag = 0
Vrijdag = 2500
Zaterdag = 5000
Zondag = 3500
Dagen_week = [Maandag,Dinsdag,Woensdag,Donderdag,Vrijdag,Zaterdag,Zondag]
Weekopbrengst = inkomsten_totaal(Dagen_week)
print()
print(Weekopbrengst)
#Huiswerkopdracht 7
def inkomsten_totaalbtw(inkomsten,btw): 
    inkomsten_totaal = 0          
    for dagen in inkomsten:
        inkomsten_totaal += dagen
    btwafdracht = inkomsten_totaal * btw
    weekoverzicht = f"Het totaal van alle inkomsten van deze week is {inkomsten_totaal} euro, waarover {btwafdracht:.2f} euro btw betaald dient te worden"
    return weekoverzicht
btw = 0.09
financieel_verslag = inkomsten_totaalbtw(Dagen_week, btw)
print()
print(financieel_verslag)

#Huiswerkopdracht 8
def laag_en_hoog(mijn_lijst):
    minmax_lijst = []
    minimaal = min(mijn_lijst)
    maximaal = max(mijn_lijst)
    minmax_lijst.append(maximaal)
    minmax_lijst.append(minimaal)
    return minmax_lijst
    
minmax = laag_en_hoog(Dagen_week)
print()
print(minmax)

#Huiswerkopdracht 9
def gemiddelde(mijn_lijst):
    average = sum(mijn_lijst) / len(mijn_lijst)
    return average

gem = gemiddelde(Dagen_week)
print()
print(gem)

#Huiswerkopdracht 10
def gemiddelde(mijn_lijst):
    average = sum(mijn_lijst) / len(mijn_lijst)
    uitvoer = f"De gemiddelde inkomsten per dag zijn deze week {average} euro"
    return uitvoer

stringgem = gemiddelde(Dagen_week)
print()
print(stringgem)

#Huiswerkopdracht 11
def meervoudig(invoerlijst):
    minmaxlijst = laag_en_hoog(invoerlijst)
    return minmaxlijst
lijst_algemeen = [0,5,8,7,3,2,1,45,6,-5]
benbenieuwd = meervoudig(lijst_algemeen)
print()
print(benbenieuwd)

#Huiswerkopdracht 12
def combinatie(invoer_lijst_2):
    korte_lijst = meervoudig(invoer_lijst_2)
    mini = min(korte_lijst)
    maxi = max(korte_lijst)
    uitvoer = mijn_functie2(maxi, mini)
    return uitvoer

lijst_2 = [51,36,91,74,144,12,15,88,99,100]
les8 = combinatie(lijst_2)
print()
print(les8) 