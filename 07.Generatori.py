'''
Napraviti generator funkcije za ispis svih parnih
i svih neparnih brojeva manjih od prosljeđenog parametra.
'''

def parni_neparni(broj):
    rezultati = []
    for i in range(broj):
        if i % 2 == 0:
            rezultati.append((i, "paran"))
        else:
            rezultati.append((i, "neparan"))
    return rezultati

rezultati = parni_neparni(10)
for broj, status in rezultati:
    print("Broj: " + str(broj) + " je " + str(status))
