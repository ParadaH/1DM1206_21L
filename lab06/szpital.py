from jednostka_medyczna import JednostkaMedyczna

class Szpital(JednostkaMedyczna):

    def __init__(self, nazwa, rok_powstania, liczba_lekarzy, liczba_pielegniarek, lokalizacja):
        super().__init__(nazwa, rok_powstania, liczba_lekarzy, liczba_pielegniarek)
        self. __lokalizacja = lokalizacja
