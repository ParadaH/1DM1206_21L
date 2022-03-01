def zad2():
    determinant = 0
    matrix = [[1, 2, 3], [3, 3, 3], [2, 3, 3]]

    determinant = (matrix[0][0] * matrix[1][1] * matrix [2][2]) + (matrix[1][0] * matrix[2][1] * matrix[0][2]) + (matrix[2][0] * matrix[0][1] * matrix [2][2]) - (matrix[0][2] * matrix[1][1] * matrix[2][0]) - (matrix[1][2] * matrix[2][1] * matrix[0][0]) - (matrix[2][2] * matrix[0][1] * matrix[1][0])
    
    if (determinant == 0):
        print("Nie da się obliczyć wyznacznika!")
    else:
        determinant = 1/determinant
        print(determinant)

if __name__ == "__main__":
    zad2()