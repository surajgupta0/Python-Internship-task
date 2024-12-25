import numpy as np

def input_matrix(prompt):

    print(prompt)
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    print("Enter the elements row by row (space-separated):")
    matrix = []
    for _ in range(rows):
        row = list(map(float, input().split()))
        if len(row) != cols:
            print(f"Error: Expected {cols} elements. Try again.")
            return input_matrix(prompt)
        matrix.append(row)
    return np.array(matrix)

def display_matrix(matrix, title):
    print(f"\n{title}:")
    print(matrix)

def matrix_operations():

    print("=== Matrix Operations Tool ===")
    while True:
        print("\nChoose an operation:")
        print("1. Add Matrices")
        print("2. Subtract Matrices")
        print("3. Multiply Matrices")
        print("4. Transpose Matrix")
        print("5. Determinant of a Matrix")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            mat1 = input_matrix("Enter the first matrix:")
            mat2 = input_matrix("Enter the second matrix:")
            if mat1.shape != mat2.shape:
                print("Error: Matrices must have the same dimensions for addition.")
            else:
                result = mat1 + mat2
                display_matrix(result, "Sum of Matrices")
        
        elif choice == "2":
            mat1 = input_matrix("Enter the first matrix:")
            mat2 = input_matrix("Enter the second matrix:")
            if mat1.shape != mat2.shape:
                print("Error: Matrices must have the same dimensions for subtraction.")
            else:
                result = mat1 - mat2
                display_matrix(result, "Difference of Matrices")
        
        elif choice == "3":
            mat1 = input_matrix("Enter the first matrix:")
            mat2 = input_matrix("Enter the second matrix:")
            if mat1.shape[1] != mat2.shape[0]:
                print("Error: Number of columns in the first matrix must equal the number of rows in the second matrix.")
            else:
                result = mat1 @ mat2  # Matrix multiplication
                display_matrix(result, "Product of Matrices")
        
        elif choice == "4":
            mat = input_matrix("Enter the matrix to transpose:")
            result = mat.T
            display_matrix(result, "Transpose of the Matrix")
        
        elif choice == "5":
            mat = input_matrix("Enter the square matrix to find the determinant:")
            if mat.shape[0] != mat.shape[1]:
                print("Error: Determinant can only be calculated for square matrices.")
            else:
                result = np.linalg.det(mat)
                print(f"\nDeterminant of the Matrix: {result:.2f}")
        
        elif choice == "6":
            print("Exiting the Matrix Operations Tool. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    matrix_operations()
