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
with open("Git\\Vislice\\besede.txt", encoding="utf-8") as datoteka_bazena:
    for beseda in datoteka_bazena:
        bazen_besed.append(beseda.strip().lower())

#definiram razred
class Igra:
    #nastavim vrednost spremenljivk
    def __init__(self, geslo, crke=None):
        self.geslo = geslo.lower()
        if crke is None:
            self.crke = []
        else:
            self.crke = crke.lower()


    # Metoda za ustvarjanje seznamov pravilnih in napačnih črk
    def pravilne_crke_1(self, crke):
        seznam_pravilnih = []
        seznam_napacnih = []
        for znak in crke:
            if znak in self.geslo:
                seznam_pravilnih.append(znak)
            else:
                seznam_napacnih.append(znak)
        return seznam_napacnih, seznam_pravilnih

    # metoda, ki vrača le željeno (pravilne ali napačne)
    def napacne_crke(self):
        return [crka for crka in self.crke if crka not in self.geslo]
    
    def pravilne_crke(self):
        return  [crka for crka in self.crke if crka in self.geslo]

    # Preštejem število napačnih ugibanj
    def stevilo_napak(self):
        return len(self.napacne_crke())

    # metodi za določanje zmage ali poraza
    # Poraz
    def je_poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    #zmaga
    def je_zmaga(self):
        for crka in self.geslo:
             if crka not in self.crke:
                 return False
        return True
    
    # izpiše nepravilna ugibanja ločena s presledkom
    def nepravilni_ugibi(self):
        return " ".join(self.napacne_crke())

    # vrne pravilni del gesla, ki izpiše le uganjene črke, preostale nadomesti z "_"
    def pravilni_del_gesla(self):
        trenutno = ""
        for crka in self.geslo:
            if crka in self.crke:
                trenutno += crka
            else:
                trenutno += "_"

        return trenutno

    # metoda za ugibanje
    def ugibaj(self, ugibana_crka):
        ugibana_crka = ugibana_crka.lower()

        if ugibana_crka in self.crke:
            return PONOVLJENA_CRKA
        
        self.crke.append(ugibana_crka)

        if ugibana_crka in self.geslo:
            # je uganil:
            if self.je_zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA     

        else:
            if self.je_poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA

# funkcija, ki izbere naključno besede za novo igro
def nova_igra():
    import random
    nakljucna_beseda = random.choice(bazen_besed)
    return Igra(nakljucna_beseda)


class Vislice:
    def __init__(self):
        self.igre = {}

    def prosti_id_igre(self):

        if len(self.igre) == 0:
            return 0
        else:
            return max(self.igre.keys()) + 1

    def nova_igra(self):
        
        nov_id = self.prosti_id_igre()

        sveza_igra = nova_igra()

        self.igre[nov_id] = (sveza_igra, ZACETEK)

        return nov_id

    def ugibaj(self, id_igre, crka):

        trenutna_igra, _= self.igre[id_igre]

        novo_stanje = trenutna_igra.ugibaj(crka)

        self.igre[id_igre] = (trenutna_igra, novo_stanje)