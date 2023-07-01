'''
Napisati regex za provjeru validnosti unosa e-maila. E-Mail mora biti formata ime.prezime@fpmoz.sum.ba
Nakon toga napisati regex za provjeru eduId koji mora biti formata iprezimeX@sum.ba gdje je i prvo slovo 
imena + prezime.
X predstavlja bilo koji broj (moze ici u beskonacnost), a taj broj ne mora postojati (može biti samo 
iprezime@sum.ba).
Od korisnika zatražiti unos maila i eduid te ispisati uspješnost.
'''

import re

r_Email = '^[a-zA-Z]+\.[a-zA-Z]+@fpmoz\.sum\.ba$'
r_EduId = '^[a-z]{1}[a-zA-Z]+\d*@sum\.ba$'

unos_Email=input("| Upišite Vaš Email: ")


if re.match(r_Email, unos_Email):
    print("Upisana E-mail adresa je ispravna.")
else:
    print(" Upisana E-mail adresa nije ispravna.")

print("\n")  
unos_EduId=input("| Upišite Vaš EduId: ")

if re.match(r_EduId, unos_EduId):
    print("Uspješna prijava")
else:
    print("Pogrešna prijava")
