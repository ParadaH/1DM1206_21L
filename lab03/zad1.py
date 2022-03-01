import math

def zasieg():
    wspolrzedne = [(2, 2), (3, 5), (5, 7), (4, 3), (1, 5), (5, 0), (10, 0), (12, 4)]

    wspolrzedne_dobre = list(filter(lambda x: 5 < math.sqrt(x[0]**2 + x[1]**2) < 10, wspolrzedne))
    odleglosci_wspolrzednych = list(map(lambda x: math.sqrt(x[0]**2 + x[1]**2), wspolrzedne))
    print("Odleglosci od (0,0):", odleglosci_wspolrzednych, "\n")

    print("Odleglosci punktów spełniajacych zadanie:")
    for i in range(len(wspolrzedne)):
        if (5 < odleglosci_wspolrzednych[i] < 10):
            print(odleglosci_wspolrzednych[i])

    print("Wspolrzedne spelniajace warunki:", wspolrzedne_dobre)

if __name__ == "__main__":
    zasieg()