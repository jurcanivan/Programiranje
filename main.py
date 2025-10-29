STOP_WORDS = ['i', 'u', 'na', 'je', 'se', 'su', 's', 'za', 'o', 'a', 'pa', 'te', 'li', 'da', 'ali', 'bi', 'bilo', 'što', 'ga', 'mu', 'joj', 'ih']

# Funkcija koja učitava tekst iz datoteke
def ucitaj_tekst(filepath):  
    """Učitava tekst iz zadane datoteke i vraća ga kao string."""  
    try:  
        with open(filepath, 'r', encoding='utf-8') as file:  # otvaramo datoteku za čitanje u UTF-8 formatu
            return file.read()  # čitamo cijeli sadržaj datoteke
    except FileNotFoundError:  # ako datoteka ne postoji
        print(f'Greška: Datoteka "{filepath}" ne postoji.')  # ispisujemo poruku o grešci
        return None  # vraćamo None da signaliziramo grešku

# Funkcija koja čisti tekst od interpunkcije i pretvara u mala slova
def ocisti_tekst(tekst):  
    """Pretvara tekst u mala slova i uklanja interpunkciju."""  
    tekst = tekst.lower()  # pretvaramo sve znakove u mala slova
    interpunkcija = ['.', ',', '!', '?', ':', ';', '"', "'", '(', ')', '-', '_', '–']  # znakovi koje želimo ukloniti
    for znak in interpunkcija:  # prolazimo kroz sve znakove
        tekst = tekst.replace(znak, '')  # brišemo ih iz teksta
    return tekst.split()  # razdvajamo riječi i vraćamo listu riječi

# Funkcija koja broji koliko se puta svaka riječ pojavljuje
def broji_frekvenciju(lista_rijeci):  
    """Vraća rječnik s riječima i njihovom frekvencijom."""  
    rjecnik_frekvencija = {}  # kreiramo prazan rječnik
    for rijec in lista_rijeci:  # prolazimo kroz svaku riječ
        rjecnik_frekvencija[rijec] = rjecnik_frekvencija.get(rijec, 0) + 1  # povećavamo broj pojavljivanja
    return rjecnik_frekvencija  # vraćamo rječnik s rezultatima

# Funkcija koja uklanja "stop-words" iz rječnika frekvencija
def ukloni_stop_words(rjecnik_frekvencija, stop_words_lista):  
    """Uklanja nebitne riječi (stop-words) iz rječnika frekvencija."""  
    ocisceni_rjecnik = {}  # stvaramo novi rječnik za filtrirane riječi
    for rijec, frekvencija in rjecnik_frekvencija.items():  # prolazimo kroz sve parove (riječ, frekvencija)
        if rijec not in stop_words_lista:  # ako riječ nije u listi stop-words
            ocisceni_rjecnik[rijec] = frekvencija  # dodajemo je u novi rječnik
    return ocisceni_rjecnik  # vraćamo očišćeni rječnik

# Funkcija koja sortira rječnik po frekvenciji i ispisuje najčešće riječi
def sortiraj_i_ispisi(rjecnik_frekvencija, broj_rijeci=15):  
    """
    Sortira rječnik po frekvenciji (od najveće prema najmanjoj)
    i ispisuje top 'broj_rijeci' rezultata.
    """  
    # pretvaramo rječnik u listu parova i sortiramo po vrijednosti (frekvenciji)
    sortirana_lista = sorted(rjecnik_frekvencija.items(), key=lambda item: item[1], reverse=True)  

    print("\n--- Top", broj_rijeci, "najčešćih riječi ---")  # ispis zaglavlja
    for i, (rijec, frekvencija) in enumerate(sortirana_lista[:broj_rijeci]):  # prolazimo kroz prvih N riječi
        print(f"{i+1}. {rijec}: {frekvencija}")  # ispisujemo redni broj, riječ i broj ponavljanja
    print("-" * 40)  # ispis linije razdjelnika

# Glavni dio programa – pokreće se samo ako se datoteka izvršava direktno
if __name__ == '__main__':  
    filepath = 'tekst.txt'  # naziv datoteke iz koje čitamo tekst
    print(f'Učitavam tekst iz datoteke: {filepath}')  # informacija korisniku

    ucitani_tekst = ucitaj_tekst(filepath)  # poziv funkcije za učitavanje teksta
    if not ucitani_tekst:  # ako nije učitano (None ili prazan string)
        print('Program se prekida jer tekst nije učitan.')  # ispis poruke
        exit()  # prekid programa

    print('\nTekst uspješno učitan!')  # potvrda da je sve u redu
    print('-' * 40)  # ispis crte
    print(ucitani_tekst)  # ispis učitanog sadržaja
    print('-' * 40)  # ispis crte

    procisceni_tekst = ocisti_tekst(ucitani_tekst)  # poziv funkcije za čišćenje teksta
    print("\nPročišćeni tekst:")  # naslov
    print(procisceni_tekst)  # ispis liste riječi nakon čišćenja

    broj_rijeci = broji_frekvenciju(procisceni_tekst)  # brojimo pojavljivanja riječi
    print("\n--- Rječnik frekvencija ---")  # naslov
    print(broj_rijeci)  # ispis rječnika s rezultatima

    ociscene_frekvencije = ukloni_stop_words(broj_rijeci, STOP_WORDS)  # uklanjamo stop-words
    print("\n--- Očišćeni rječnik frekvencija ---")  # naslov
    print(ociscene_frekvencije)  # ispis rječnika bez nevažnih riječi

    sortiraj_i_ispisi(ociscene_frekvencije, broj_rijeci=15)
