'''
Iz podataka učitanih u prethodnom primjeru sortirati listu po prezimenima.
Napraviti novi rječnik gdje će se po bodovnom rangu upisivati broj ostvarenih ocjena. 
Nedovoljan
0-49%
Dovoljan
50-65%
Dobar
65-80%
Vrlodobar
80-90%
Izvrstan
90-100%
'''
import csv

with open('rezultati.csv', 'r') as file:
    redovi = file.readlines()
    studenti = []
    for linija in redovi:
        elementi = linija.strip().split(';')
        ime, prezime, bodovi, = elementi
        print (tuple(elementi))
        studenti.append((ime, prezime, int(bodovi)))

sortirano=sorted(studenti, key=lambda x: x[1])

ocjene={
    "Odličan":[],
    "Vrlodobar":[],
    "Dobar":[],
    "Dovoljan":[],
    "Nedovoljan":[]
    }


for ime,prezime, bodovi in sortirano:
    if bodovi > 91:
        ocjene["Odličan"].append(prezime)
    elif bodovi > 81:
        ocjene["Vrlodobar"].append(prezime)
    elif bodovi > 66:
        ocjene["Dobar"].append(prezime)
    elif bodovi > 50:
        ocjene["Dovoljan"].append(prezime)
    else:
        ocjene["Nedovoljan"].append(prezime)


print(ocjene)
