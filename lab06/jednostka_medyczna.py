
#klasa_bazowa
class JednostkaMedyczna:

    def __init__(self, nazwa, rok_powstania, liczba_lekarzy, liczba_pielegniarek):
        self.__nazwa = nazwa
        self.__rok_powstania = rok_powstania
        self.__liczba_lekarzy = liczba_lekarzy
        self.__liczba_pielegniarek = liczba_pielegniarek

    def wyciagnij_nazwa(self):
        return self.__nazwa

    def wyciagnij_rok_powstania(self):
        return self.__rok_powstania

    def __repr__(self):
        cls_nazwa = self.__class__.__name__
        attrs = {k.split("__")[-1]: v for k, v in self.__dict__.items()}
        return f"(({cls_nazwa}): {attrs})"
