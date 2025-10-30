"""
moja_lista = []
moja_lista.append(10)
moja_lista.append(20)
moja_lista.append(30)

print(moja_lista[1])

print(moja_lista[0:2])

moja_lista.remove(20)

print(moja_lista)

Zadatak1

voce = ["jabuka", "banana", "kruska"]
print(voce[0])
voce.append("naranca")
print(voce)




# Ovo je 2D lista (3 retka, 3 stupca)
ormar = [
    ['majica', 'kapa', 'sal'],    # 0. redak (polica)
    ['hlace', 'carape', 'remen'], # 1. redak
    ['jakna', 'cipele', 'cizme']  # 2. redak
]

for redak in ormar:
    print(redak[1])
"""
def pronadi_broj(lista, trazeni_broj):
    for element in lista:
        if element == trazeni_broj:
            provjera = True
            break

    if provjera:
        print(f"Broj {trazeni_broj} je na listi.")
    else:
        print(f"Broj {trazeni_broj} nije na listi.")

provjera = False

lista_brojeva = [10, 20, 30, 40, 50]
trazeni_broj = 30

pronadi_broj(lista_brojeva, trazeni_broj)
