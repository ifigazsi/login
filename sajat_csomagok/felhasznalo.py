
db = {}
probak_szama = {}
probalkozasok_max_szama = 3

def belepes():
    print(f"\n{'*' * 25}\nBELEPES")
    felhasznalonev, jelszo = felhasznalonev_es_jelszo_bekerese()
    if belepesi_adatok_megfeleloek(felhasznalonev, jelszo):
        return
    belepes()


def regisztracio():
    print(f"\n{'*' * 25}\nREGISZTRACIO")
    felhasznalonev, jelszo = felhasznalonev_es_jelszo_bekerese()
    if foglalt_a_felhasznalonev(felhasznalonev):
        regisztracio()
    hozzaadas(felhasznalonev, jelszo)
    belepes()


def felhasznalonev_es_jelszo_bekerese():
    felhasznalonev = input("Add meg a felhasznaloneved: ")
    jelszo = input("Add meg a jelszavad: ")
    return felhasznalonev, jelszo


def regisztracio_vagy_belepes():
    print("*" * 25)
    print("\nKezdokepernyo")
    valasz = input("Van már regisztrációd? (igen/nem) ").lower().strip()
    utvalaszto = {"igen": belepes, "nem": regisztracio}
    funk = utvalaszto.get(valasz, regisztracio_vagy_belepes)
    funk()


def belepesi_adatok_megfeleloek(felhasznalonev, jelszo):
    if felhasznalonev in db.keys() and jelszo == db[felhasznalonev]:
        probalkozasok_szamanak_nullazasa(felhasznalonev)
        return True
    probalkozasok_szamanak_novelese(felhasznalonev)
    print("HIBAS FELHASZNALONEV VAGY JELSZO")
    return False

def probalkozasok_szamanak_novelese(felhasznalonev):
    probak_szama[felhasznalonev] = probak_szama.get(felhasznalonev, 0) + 1
    if probak_szama[felhasznalonev] == probalkozasok_max_szama:
        exit("Tul sok probalkozas")

def probalkozasok_szamanak_nullazasa(felhasznalonev):
    probak_szama[felhasznalonev] = 0

def foglalt_a_felhasznalonev(felhasznalonev):
    if felhasznalonev in db.keys():
        print("A választott felhasznalonev mar foglalt")
        return True
    return False

def hozzaadas(felhasznalonev, jelszo):
    db[felhasznalonev] = jelszo







