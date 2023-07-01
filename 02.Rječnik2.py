'''
Koristeći listu imena iz prethodnog zadatka svakom studentu generirati nasumičnu ocjenu od 1 do 5.
Prebrojati u rječnik koliko ima kojih ocjena.
Izračunati postotak prolaznosti. (sve ocjene veće od 1)
'''

import random

imena = ['Karlo', 'Ana-Marija', 'Antonio', 'Marko', 'Matea', 'Vice', 'Sara', 'Ivana', 'Ante', 'Ivan Entoni', 'Tonka', 'Antonio',
         'Mateo', 'Mateo', 'Josip', 'Marko', 'Tino', 'Azer', 'Tomislava', 'Katarina', 'Karlo', 'David', 'Ivan', 'Petar', 'Marija',
         'Antonio', 'Mario', 'Josip', 'Leonardo', 'Antonio', 'Renato', 'Matej', 'Matej', 'Jozo Matej', 'Petar', 'Ivan', 'Stjepan',
         'Petar', 'Dražen', 'Zvonimir', 'Marin', 'Antonio', 'Stipe', 'Ana', 'Mate', 'Miroslav', 'Karlo', 'Marino', 'Mija', 'Kristijan',
         'Ante', 'Ana', 'Iva', 'Mladen', 'Ivan', 'Frano', 'Mate', 'Mateo', 'Harun']

ocjenes = {}
prebrojano = {5: 0, 4: 0, 3: 0, 2: 0, 1: 0}

ocjene = [random.randint(1, 5) for _ in imena]
ocjenes = dict(zip(imena, ocjene))

prebrojano = {ocjena: ocjene.count(ocjena) for ocjena in ocjene}

print(prebrojano)

brojac = sum(ocjena * prebrojano[ocjena] for ocjena in prebrojano if ocjena > 1)
brocjena = sum(prebrojano[ocjena] for ocjena in prebrojano if ocjena > 1)

prosjecna = brojac / brocjena
print(prosjecna)
