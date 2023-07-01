'''
Potrebno napisati regex koji vraca podudaranje ukoliko se unese string koji počinje kao prvo slovo vašeg imena, a završava kao prvo slovo 
prezimena. String mora sadržavati bar jedan broj između 0 i 5 i razmak.
'''
import re

regex = r"^[Aa].*[0-5].*\s.*[Ss]$"

unos = input("Unesite string: ")

if re.match(regex, unos):
    print("String zadovoljava kriterije.")
else:
    print("String ne zadovoljava kriterije.")
