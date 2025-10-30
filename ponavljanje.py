"""
Ovo je višeredni komentar
"""
# -*- coding: utf-8 -*-

#Ovo je jednolinijski komentar

#1. tipovi podataka

broj = 10 #int(integer) - cijeli broj
tekst = "Ovo je rečenica." #string (tekst) - niz znakova
znak = 'a' #char (character) - znak
cijena = 1.5 # float - decimalni broj
instina = True # bool (boolean) - True/False



# Grananje (if/elif/else)
"""
if broj > 5:
    print("Broj je veći pd 5") 
elif broj == 5:
    print("Broj je jednak 5 ")
else:
    print("Broj je manji od 5")

if not instina:
    print("False")
else:
    print("True")

"""

#Zadatak 1: Grananje u praksi (temperatura)
"""
print("Upiši trenutnu temperaturu")
temperatura = input()
temperatura = int(temperatura)
"""
"""
temperatura = int (input("Upiši trenutu temperaturu: "))

if temperatura <= 0:
    print("Ledenica")
elif temperatura > 0 and temperatura <= 15:
    print("Hladno")
elif temperatura < 16 and temperatura <= 25:
    print("Ugodno")
else:
    print("Vruće")
    """

#Petlje

for i in range (2, 23):
    if i % 2 == 0:
        print(f"{i} je paran broj.")
    else:
        print(f"{i} je neparan broj.")
