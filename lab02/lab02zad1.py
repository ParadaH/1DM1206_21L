def zad1(tab_1, tab_2):
    tab_3 = ""

    if len(tab_1)>len(tab_2):
        length = len(tab_2)
    else:
        length = len(tab_1)
    for i in range(length):
        tab_3 = tab_3 + tab_1[i] + tab_2[i]

    tab_3 = tab_3 + tab_2[i+1:]
    print(tab_3)

if __name__ == "__main__":
    zad1("ABC", "DEFGHI")