def cislo_text(cislo):
    cislo = int(cislo)

    jednotky = [
        "nula", "jedna", "dva", "tři", "čtyři", 
        "pět", "šest", "sedm", "osm", "devět",
        "deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", 
        "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"
    ]

    desitky = [
        "", "", "dvacet", "třicet", "čtyřicet", 
        "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"
    ]

    if cislo < 20:
        return jednotky[cislo]
    elif cislo < 100:
        pocet_desitek = cislo // 10
        pocet_jednotek = cislo % 10
        if pocet_jednotek == 0:
            return desitky[pocet_desitek]
        else:
            return desitky[pocet_desitek] + " " + jednotky[pocet_jednotek]
    elif cislo == 100:
        return "sto"


if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)
