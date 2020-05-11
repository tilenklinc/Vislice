import model

trenutna_igra = model.nova_igra()
# ob porazu:

def izpis_poraza(igra):
    return f"IZGUBIL SI, geslo je bilo: {igra.geslo}"

# ob zmagi
def izpis_zmage(igra):
    return (f"ZMAGAL SI, geslo je bilo: {igra.geslo}," +
    f"potreboval si {len(igra.napacne_crke())} ugibov")

def izpis_igre(igra):
    text = (
        f"Stanje gesla: {igra.pravilni_del_gesla()} \n"
        f"Imaš še {model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak()} možnosti za napako"
    )

    return text


def zahtevaj_vnos():
    return input("Vpiši naslednjo črko:")


def pozeni_vmesnik():
    #naredimo novo igro
    trenutna_igra = model.nova_igra()

    while True:
        print(izpis_igre(trenutna_igra))

        crka = zahtevaj_vnos()

        rezultat = trenutna_igra.ugibaj(crka)

        if trenutna_igra.zmaga():
            print(izpis_zmage(trenutna_igra))
            break

        if trenutna_igra.poraz():
            print(izpis_poraza(trenutna_igra))
            break


pozeni_vmesnik()