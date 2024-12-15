#Huiswerkopdracht 2
prijzen = {
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" : 5
}
#Huiswerkopdracht 3
aanbieding = prijzen["aardbei"] * 0.8
aanbieding = round(aanbieding,2)
#Huiswerkopdracht 4
euro_teken = "\u20AC"
reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts {euro_teken} {aanbieding}"
print(reclame_tekst)
#Huiswerkopdracht 5
print()
reclame_tekst2 = reclame_tekst[:62]
print(reclame_tekst2)
#Huiswerkopdracht 6
print()
reclame_tekst3 = reclame_tekst2.upper()
print(reclame_tekst3)
#Huiswerkopdracht 7
reclame_tekst4 = reclame_tekst3.split()
print(reclame_tekst4)
#Huiswerkopdracht 8
print()
for el in reclame_tekst4:
    print(el)
#Huiswerkopdracht 9
print()
for el in reclame_tekst4:
    print(el.lower())
#Huiswerkopdracht 10
print()
for el in reclame_tekst4:
    aantal = len(el)
    if aantal > 4:
        print(el.upper())
    else:
        print(el.lower())
    

