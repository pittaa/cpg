def je_prvocislo(cislo):
    """
    Funkce ověří, zda zadané číslo je prvočíslo, a vrátí True nebo False.
    """
    cislo = int(cislo)
    
    # Prvočísla jsou pouze celá čísla větší než 1
    if cislo <= 1:
        return False

    # Stačí testovat dělitele do odmocniny z čísla (včetně)
    for delitel in range(2, int(cislo ** 0.5) + 1):
        if cislo % delitel == 0:
            return False

    return True


def vrat_prvocisla(maximum):
    """
    Funkce vrátí seznam všech prvočísel v rozsahu 1 až maximum (včetně).
    """
    maximum = int(maximum)
    vysledky = []

    for i in range(2, maximum + 1):
        if je_prvocislo(i):
            vysledky.append(i)

    return vysledky


if __name__ == "__main__":
    cislo = input("Zadej maximum: ")
    prvocisla = vrat_prvocisla(cislo)
    print(prvocisla)
