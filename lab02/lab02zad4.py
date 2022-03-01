if __name__ == "__main__":
    f = open("Pzcpd.txt", "r")

    for line in f:
        print(line[14:-5])

    f = fclose