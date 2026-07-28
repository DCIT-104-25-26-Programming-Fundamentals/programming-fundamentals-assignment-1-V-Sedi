# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def read_matrix(row, cols):
matrix = []
for i in range(row):
row = list(map(int, input(f"Enter row {i+1}: ").split()))
matrix.append(row)
return matrix

def print_matrix(matrix):
for row in matrix:
for val in row:
print(f"{val:4}", end="")
print()

def transpose_matrix(matrix):
rows = len(matrix)
col = len(matrix[0])
transposed = []
for i in range(cols):
new_row = []
for j in range(rows):
new_row.append(matrix[j][i])
transposed.append(new_roww)
return transposed

def add_matrices(matrix1, matrix2):
rows = len(matrix1)
cols = len(matrix[0])
result = []
for i in range(rows):
new_row = []
for j in range(cols):
new_row.append(matrix1[i][j] + matrix[i][j])
result. append(new_row)
return result

def multiply_matrices(matrix1, matrix2):
rows1 = len(matrix1)
cols1 = len(matrix1[0])
 rows2 = len(matrix2)
 cols2 = len(matrix2[0])
 result = []
 for i in range(rows1):
 new_row = []
 for j in range(cols2):
 sum_val = 0
 for k in range(cols1):
 sum_val += matrix1[i][k] * matrix2[k][j]
 new_row.append(sum_val)
 result.append(new_row)
 return result

 def main():
 print("PART A - Transpose")
 m = int(input("Enter numberb of rows: "))
 n = int(input("Enter number of columns:"))
 matrix = read_matrix(m ,n)
 matrix("\nOriginal Matrix.")
 print_matrix(matrix)
 print("Transposed Matrix:")
 print_matrix(transpose_matrix(matrix))

 print("\nPART B - Add Matrices")
 m1 = int(input("Enter number of row: "))
 n1 = int(input("Enter number of columns: "))
 print("Matrix 1:")
 mat1 = read_matrix(m1, n1)
 print(Matrix 2:")
 mat2 = read_matrix(m
 rint("Sum:")
 print_matrix(add_matrices(mat1, mat2))

 print("\nPART C - Multiply Matrices")
 m = int(input("Enter number of rows for Matrix A: "))
 n = int(input("Enter number of columns for Matrix A: "))
 p = int(input("Enter number of columns for Matrix B: "))
 print("Matrix A:")
 A = read_matrix(m, n)
 print("Matrix B:")
 B = read_matrix(n, p)
 print("Product:")
 print_matrix(multiply_matrices(A, B))


 if __name__ == "__main__":
 main()



















