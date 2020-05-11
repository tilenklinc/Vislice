# Konstante za rezultate ugibanj:
STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = "+"
PONOVLJENA_CRKA = "o"
NAPACNA_CRKA = "-"
# Konstante za zmago in poraz
ZMAGA = "W"
PORAZ = "X"

# Odpremo datoteko in ločimo besede
bazen_besed =  []
with open("Git\Vislice\\besede.txt", encoding="utf-8") as datoteka_bazena:
    for beseda in datoteka_bazena:
        bazen_besed.append(beseda.strip().lower())

#definiram razred
class Igra:
    #nastavim vrednost spremenljivk
    def __init__(self, geslo, crke=None):
        self.geslo = geslo
        if crke is None:
            self.crke = []
        else:
            self.crke = crke


    # Metoda za ustvarjanje seznamov pravilnih in napačnih črk
    def pravilne_crke(crke):
        seznam_pravilnih = []
        seznam_napacnih = []
        for znak in crke:
            if znak in self.geslo:
                seznam_pravilnih.append(znak)
            else:
                seznam_napacnih.append(znak)

    # Preštejem število napačnih ugibanj
    def stevilo_napak():
        len(seznam_napacnih)

