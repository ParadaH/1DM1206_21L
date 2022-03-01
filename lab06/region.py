from jednostka_medyczna import JednostkaMedyczna


class Region:

    def __init__(self):
        self.lista = []

    def dodaj(self, jednostka: JednostkaMedyczna):
        self.lista.append(jednostka)

    def wypisz_posortowane_po_nazwie(self):
        self.lista = sorted(self.lista, key=lambda x: x.wyciagnij_nazwa())

    def wypisz_posortowane_po_dacie(self):
        self.lista = sorted(self.lista, key=lambda x: x.wyciagnij_rok_powstania())

    def __add__(self, other):
        self.lista = self.lista + other.lista
        return self

    def wypisz(self):
        for i in self.lista:
            print("{} ->".format(i.__class__.__name__), end=" ")
            res = " | ".join([f"{k.split('__')[-1]}: {v}" for k, v in i.__dict__.items()])
            print(res)

    def __repr__(self):
        cls_name = self.__class__.__name__
        attrs = {k.split("__")[-1]: v for k, v in self.__dict__.items()}
        return f"(({cls_name}): {attrs})"
