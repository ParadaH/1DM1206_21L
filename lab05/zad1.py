# 1. Proszę stworzyć klasę Człowiek składającą się z pól: imię, nazwisko, wiek.
# 2. Proszę stworzyć klasę Wycieczka składającą się z pól:
#       opiekun, uczestnicy. Pole opiekun ma być obiektem klasy Człowiek.
#       Pole uczestnicy ma być listą obiektów klasy Człowiek.
# 3. W klasie człowiek proszę nadpisać operację dodawania w taki sposób,
#       że w wyniku dodawania obiektu B do obiektu A (A+B) powstanie nowy obiekt klasy Wycieczka,
#       w którym opiekunem będzie opiekun z obiektu A, a uczestnikami będą uczestnicy
#       z dwóch obiektów Wycieczka (A, B).
# 4. Do klasy Wycieczka proszę dopisać metodę, która będzie czytelnie wypisywała zawartość
#       klasy Wycieczka (w pierwszym wierszu: opiekun; w pozostałych wierszach,
#       w "tabeli", uczniowie: imię, nazwisko, wiek).
#       Proszę zachować stałą szerokość poszczególnych pól w "tabeli"
#
#       Opiekun: Jan Philips
#       Uczestnicy:
#       | imię | nazwisko | wiek |
#       ==========================
#       |  Abc |      Xyz |   12 |
#       |  Jan |     Nikt |   14 |

# 5. Proszę przygotować dwie wycieczki z przynajmniej dwoma uczestnikami każda z nich.

from czlowiek import Czlowiek
from wycieczka import Wycieczka

if __name__ == "__main__":
    czlowiek_1 = Czlowiek("Jan", "Mela", "45")
    czlowiek_2 = Czlowiek("Herbert", "Parada", "19")
    czlowiek_3 = Czlowiek("Charmeleon", "Charizard", "25")
    czlowiek_4 = Czlowiek("Dragonite", "Dragonair", "3")
    czlowiek_5 = Czlowiek("Bulbasaur", "Ivysaur", "68")
    czlowiek_6 = Czlowiek("Wartortle", "Blastoise", "77")
    czlowiek_7 = Czlowiek("Pikachu", "Raichu", "111")
    czlowiek_8 = Czlowiek("Miltank", "Stanler", "23")
    czlowiek_9 = Czlowiek("Pink", "Floyd", "58")

    wycieczka_1 = Wycieczka(czlowiek_1)
    wycieczka_1.add_student(czlowiek_5)
    wycieczka_1.add_student(czlowiek_6)
    wycieczka_1.add_student(czlowiek_3)

    wycieczka_2 = Wycieczka(czlowiek_2)
    wycieczka_2.add_student(czlowiek_7)
    wycieczka_2.add_student(czlowiek_8)
    wycieczka_2.add_student(czlowiek_4)

    # wycieczka_1.display_table()
    # wycieczka_2.display_table()

    wycieczka_3 = wycieczka_1 + wycieczka_2
    wycieczka_3.display_table()