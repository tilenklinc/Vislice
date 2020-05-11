# Konstante:

stevilo_dovoljenih_napak = 10
pravilna_crka = "+"
ponovljena_crka = "○"
napacna_crka = "-"
zmaga = "W"
poraz = "L"

#definiram razred
class Igra:
    #nastavim vrednost spremenljivk
    def __init__(self, geslo, crke):
        self.geslo = geslo
        self.crke = poskusi_igralca


    #definiram metodi
    def pravilne_crke(poskusi_igralca):
        seznam_pravilnih = []
        seznam_napacnih = []
        for znak in poskusi_igralca:
            if znak in self.geslo:
                seznam_pravilnih.append(znak)
            else:
                seznam_napacnih.append(znak)
