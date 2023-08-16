def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(num * num)  # Compute the square value and add to new row
        new_matrix.append(new_row)  # Add new row to the new matrix
    return new_matrix

# Test the function with the provided example
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
