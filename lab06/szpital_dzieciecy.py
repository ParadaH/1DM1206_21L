from szpital import Szpital

class SzpitalDzieciecy(Szpital):

    def __init__(self, nazwa, rok_powstania, liczba_lekarzy, liczba_pielegniarek, lokalizacja, liczba_karetek):
        super().__init__(nazwa, rok_powstania, liczba_lekarzy, liczba_pielegniarek, lokalizacja)
        self.__liczba_karetek = liczba_karetek


