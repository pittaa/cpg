def sude_nebo_liche(cislo: int) -> None:
    """Otestuje, zda je zadané celé číslo sudé nebo liché, a vypíše výsledek."""
    if cislo % 2 == 0:
        print(f"Číslo {cislo} je sudé")
    else:
        print(f"Číslo {cislo} je liché")


if __name__ == "__main__":
    sude_nebo_liche(5)
    sude_nebo_liche(1000000)
