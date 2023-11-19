# midterm assignment exercise 1 (+ ex2 & ex3)
# author: Lola Jo Ackermann    

m1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# singular 3x3 matrix 
m2 = [
    [1, 2],
    [1, 2]
]
# singular 2x2 matrix
m3 = [
    [1, 5, 3],
    [-1, 9, 6],
    [6, 8, -5]
]
# invertible 3x3 matrix
m4 = [
    [0, 1, 3],
    [0, 0, 0],
    [7, 4, 0]
]
# singular 3x3 matrix
m5 = [
    [1, 5, 3, 4],
    [-1, 9, 6, -1],
    [6, 8, -5, 3],
    [1, 1, 1, 1]
]
# invertible 4x4 matrix
m6 = [
    [1, 2, 3],
    [2, 4, 5],
    [-1, -1, -1]
]
# invertible 3x3 matrix
m7 = [
    [1, 5, 3, 4, 2],
    [-1, 9, 6, -1, -3],
    [6, 8, -5, 3, 11],
    [1, 2, 4, 3, -10],
    [-11, -25, 33, 0, 2]
]
# invertible 5x5 matrix
m8 = [
    [1, 2],
    [3, 4]
]
# invertible 2x2 matrix
m9 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
# invertible 3x3 matrix
m10 = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]
# invertible 3x3 identity matrix

matrix_ex2 = [
    [1, -3, -7],
    [-1, 5, 6],
    [-1, 3, 10]
]
vector_ex2 = [10, -21,-7 ]
# exercise 2 in the midterm assignemnt

matrix_ex3 = [
    [1, 2, 3],
    [0, 1, 4],
    [5, 6, 0]
]
# exercise 3 in the midterm assignemnt

def main():
    m0 = square_matrix_input()
    process_inverse(m0, "matrix0")
    # calculating the inverse of an input matrix

    process_inverse(m1, "matrix1")
    process_inverse(m2, "matrix2")
    process_inverse(m3, "matrix3")
    process_inverse(m4, "matrix4")
    process_inverse(m5, "matrix5")
    process_inverse(m6, "matrix6")
    process_inverse(m7, "matrix7")
    process_inverse(m8, "matrix8")
    process_inverse(m9, "matrix9")
    process_inverse(m10, "matrix10")
    # calculations for the inverses of 10 example matrices

    A0 = square_matrix_input()
    b0 = vector_input(len(A0))
    solution0 = solve_system_of_linear_equations(A0,"matrix0", b0)
    print(f"the solution for the system of linear equations is: {solution0}" )
    # calculating the solutions for an input of a system of linear equations

    solution1 = solve_system_of_linear_equations(matrix_ex2,"matrix_ex2", vector_ex2)
    print(f"the solution for the system of linear equations is: {solution1}" )
    # exercise 2 in the midterm assignemnt: calculating the solutions for an input of a system of linear equations

    determinant_3 = calculate_determinant(matrix_ex3)
    if determinant_3 == 0:
        print("The matrix is singular and therefore not invertible.")
    else: 
        print("The matrix is invertible.")
    # exercise 3 in the midterm assignemnt: checking wether a matrix is invertible or not

def square_matrix_input():
    try:
        dimension = int(input(f"Enter the  dimension of your square matrix: "))
        if dimension <= 0:
            raise ValueError("The dimension must be a value greater than zero")
        
        matrix = []
        for i in range(dimension):
            while True: 
                user_input_values = input(f"Enter row {i +1}/{dimension} containing {dimension} numbers separated by commas: ")
                input_row = user_input_values.split(',')

                if len(input_row) == dimension:
                    break 
                
                print(f"Each row should exactly include {dimension} numbers and they must be separated by commas.")
            
            row = [float(num) for num in input_row]
            matrix.append(row)
        
        return matrix
    
    except ValueError as e:
        print(e)   
# creates through user inputs a square matrix

def vector_input(dimension):
    try:
        vector_b =[]
        for i in range(dimension):
            while True: 
                try:
                    user_input_value = input(f"Enter Element {i +1}/{dimension} for vector b: ")
                    user_input_value = float(user_input_value)
                    vector_b.append(user_input_value)
                    break
                except ValueError:
                    print("Invalid input. Please retry.")
            
        return vector_b
    
    except ValueError as e:
        print(e)   
# creates through user inputs vector b

def check_square_matrix (matrix):
    number_of_rows = len(matrix)
    for row in matrix:
        if len(row) != number_of_rows:
            return False
    return True
# checks if the matrix is a square matrix

def calculate_determinant(matrix):
    dimension = len(matrix)
    if dimension == 1:
        determinant_1 = matrix[0][0]
        return determinant_1

    determinant = 0
    for i in range(dimension):
        submatrix = [row[:i] + row[i + 1:] for row in matrix[1:]] 
        # creates the submatrix 
        sign = (-1) ** i
        subdeterminant  = matrix[0][i] * calculate_determinant(submatrix)
        determinant += sign * subdeterminant

    return determinant
# calculates the determinant of the square matrix

def calculate_matrix_inverse(matrix, matrix_name):
    try:
        check_square_matrix(matrix)
        determinant = calculate_determinant(matrix)

        if determinant != 0:
            dimension = len(matrix)
            inverse_matrix = []

            adjugate_matrix = []

            for i in range(dimension):
            # loops through the rows (i)
                row = []

                for j in range(dimension):
                # loops through the columns (j)
                    minor_matrix = []

                    for row_index in range(dimension):
                        if row_index != i:
                            modified_row = matrix[row_index][:j] + matrix[row_index][j + 1:]
                            minor_matrix.append(modified_row)

                    cofactor_value = ((-1) ** (i + j)) * calculate_determinant(minor_matrix)
                    row.append(cofactor_value)

                adjugate_matrix.append(row)
            # calculates the adjugate matrix

            
            for i in range(dimension):
                row = [adjugate_matrix[j][i] / determinant for j in range(dimension)]
                inverse_matrix.append(row)
            # transposes the adjugate matrix and divides everything by the determinant

            return inverse_matrix
        else:
            print(f"{matrix_name} is singular. There is no inverse for this matrix.")
            print()
            return None

    except ValueError as e:
        print(e)
# calculates the inverse of a matrix
    
def process_inverse(matrix, matrix_name):
    try:
        if check_square_matrix(matrix):
            inverse = calculate_matrix_inverse(matrix, matrix_name)

            if inverse is not None:
                print(f"inverse of {matrix_name}:")
                for row in inverse:
                    print([round(result, 3) for result in row])
                print()

        else:
            print(f"{matrix_name} isn't a square matrix")

    except ValueError as e:
        print(e)   
# checks if it is a square matrix and if its invertible. if yes, it calculates its inverse
    
def solve_system_of_linear_equations(matrix, matrix_name, vector):
    dimension = len(matrix)
    solution = [0] * dimension

    matrix_inverse = calculate_matrix_inverse(matrix, matrix_name)
    # calculates the matrix inverse

    for i in range(dimension):
        for j in range(dimension):
            solution[i] += matrix_inverse[i][j] * vector[j]
    # multiplies the inverse of matrix A with vector b to get the solution x of the system of linear equations

    solution = [round(value, 3) for value in solution]
    return solution
# solves the system of linear equations for a given matrix A and a vector b

if __name__ == '__main__':
        main()
