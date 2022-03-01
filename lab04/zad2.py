from matplotlib import pyplot as plt

if __name__ == "__main__":
    x = []
    y = []
    filename = "insertion_sort_result.txt"
    filename = open(filename, "r")

    for i in filename:
        args = i.split()
        y.append(args[0])
        x.append(args[1])

    plt.plot(x, y, "-b")
    plt.title("Sorting")
    plt.ylabel("Number of elements")
    plt.xlabel("Duration of sorting")
    plt.tight_layout()
    plt.show()
    filename.close()