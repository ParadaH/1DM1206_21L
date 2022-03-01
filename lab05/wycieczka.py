import sys
from lab05.czlowiek import Czlowiek

class Wycieczka:

    def __init__(self, opiekun: Czlowiek):
        self.opiekun = opiekun
        self.uczestnicy = []

    def add_student(self, student: Czlowiek):
        self.uczestnicy.append(student)

    def __add__(self, other):
        self.uczestnicy = self.uczestnicy + other.uczestnicy
        return self

    def display_table(self):
        print("Opiekun: {} {}".format(self.opiekun.name, self.opiekun.surname))
        header = "| {:^10} | {:^10} | {:^3} |".format("imie", "nazwisko", "wiek")
        l = len(header)
        row_length = "{}{}{}".format("+", (l - 2) * "-", "+")
        print(row_length)
        print(header)
        print(row_length)

        sorted_students = sorted(self.uczestnicy, key=lambda uczestnicy: uczestnicy.surname[1])

        for uczestnicy in sorted_students:
            print("| {:^10} | {:^10} | {:^4} |".format(uczestnicy.name, uczestnicy.surname, uczestnicy.age))

        print(row_length, "\n")
