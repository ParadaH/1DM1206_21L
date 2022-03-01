# Proszę stworzyć klasy: JednostkaMedyczna (klasa bazowa), Szpital (klasa pochodna dla klasy JednostkaMedyczna), SzpitalDziecięcy (klasa pochodna dla klasy Szpital).
# Klasa JednostkaMedyczna powinna mieć pola: nazwa, rok powstania, liczba lekarzy, liczba pielęgniarek.
# Każda klasa pochodna ma rozszerzać o dodatkowe pola (przynajmniej jedno pole) klasę nadrzędną. Proszę samodzielnie zdecydować o tych dodatkowych polach. (Szpital może mieć na przykład flagę określającą czy jest to szpital jednoimienny.)
# Proszę napisać klasę, w której będzie przechowywana lista wszystkich JednostekMedycznych (czyli również szpitali i szpitali dziecięcych). Ta klasa powinna mieć metodę umożliwiającą wypisanie całej zawartości listy. Wszystkie klasy (JednostkaMedyczna, Szpital, SzpitalDziecięcy) podczas wypisywania powinny być poprzedzone unikalną nazwą charakteryzującą daną klasę.
# Klasa z punktu 4. powinna mieć metodę umożliwiającą wpływanie na obecny stan kolekcji (na sortowanie listy ze względu na: nazwę jednostki medycznej, rok powstania jednostki medycznej).
# Proszę przestrzegać zasad hermetyzacji.
# Proszę zadbać o estetykę rozwiązania.

from region import Region
from jednostka_medyczna import JednostkaMedyczna
from szpital import Szpital
from szpital_dzieciecy import SzpitalDzieciecy

if __name__ == "__main__":

    Warszawa_1 = JednostkaMedyczna("Sympatycy Medyczni im. Mikolaj Kopernik", 1867, 204, 501)
    Warszawa_2 = JednostkaMedyczna("Grupa Medyczna im. Marii Sklodowskiej-Curie", 1950, 144, 89)
    Warszawa_3 = Szpital("Warszawski Uniwersytet Medyczny", 2012, 30, 20, "Warszawa")
    Gdansk_1 = Szpital("Szpital Akademicki w Gdansku", 1990, 279, 99, "Gdańsk")
    Torun_1 = SzpitalDzieciecy("Szpital Onkologiczny im. Bohaterow Westerplatte", 2001, 80, 30, "Toruń", 4)
    Gdynia_1 = JednostkaMedyczna("Szpital Główny w Gdyni", 1953, 121, 40)
    Sopot_1 = Szpital("Szpital Wojskowy", 1979, 10, 5, "Sopot")
    Sopot_2 = SzpitalDzieciecy("Szpital Bartosza", 1921, 10, 23, "Sopot", 1)
    # print(Warszawa_1)
    # print(Gdansk_1)
    # print(Torun_1)
    Mazowieckie = Region()
    Pomorskie = Region()

    Mazowieckie.dodaj(Warszawa_1)
    Mazowieckie.dodaj(Warszawa_2)
    Mazowieckie.dodaj(Warszawa_3)

    Pomorskie.dodaj(Gdansk_1)
    Pomorskie.dodaj(Torun_1)
    Pomorskie.dodaj(Gdynia_1)
    Pomorskie.dodaj(Sopot_1)
    Pomorskie.dodaj(Sopot_2)

    Pomorskie.wypisz_posortowane_po_nazwie()
    Pomorskie.wypisz()

    print()

    Pomorskie.wypisz_posortowane_po_dacie()
    Pomorskie.wypisz()