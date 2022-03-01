import random
from timeit import default_timer as timer

def random_list(list):
    start = 1
    end = 10000
    for i in range(random.randint(start, end)):
        list.append(random.randint(start, end))

def measure_time_decor(func_to_measure):
    def wrapper(*args, **kwargs):
        start = timer()
        result = func_to_measure(*args, **kwargs)
        end = timer()
        duration = end - start
        print("Execution time: {}".format(duration))
        f.write(" {}\n".format(duration))
        return result

    return wrapper

@measure_time_decor
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

if __name__ == "__main__":
    list = []
    random_list(list)

    filename = "insertion_sort_result.txt"
    with open(filename, "a") as f:
        for i in range(20):
            f.write("{}".format(len(list)))
            insertionSort(list)
    f.close()

    print(list)