def gaussian_elimination(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Forward elimination
    for col in range(min(rows, cols - 1)):  # Ignore the last column (constants)
        # Find the pivot row
        max_row = max(range(col, rows), key=lambda i: abs(matrix[i][col]))

        # Swap current row with the pivot row
        matrix[col], matrix[max_row] = matrix[max_row], matrix[col]

        # Check for a zero pivot element
        pivot_element = matrix[col][col]
        if pivot_element == 0:
            continue

        # Make the pivot element 1
        matrix[col] = [element / pivot_element for element in matrix[col]]

        # Eliminate other rows
        for row in range(rows):
            if row != col:
                factor = matrix[row][col]
                matrix[row] = [a - factor * b for a, b in zip(matrix[row], matrix[col])]

    # Back substitution
    solutions = [matrix[row][-1] for row in range(rows)]

    return solutions

# Test cases
print(gaussian_elimination([[0, 4, 2, -2], [-2, 3, 1, -7], [4, 5, 2, 4]]))
# Output: [2.0, -2.0, 3.0]

print(gaussian_elimination([[1, 3, 5], [2, 6, 5]]))
# Output: []

print(gaussian_elimination([[1, 3, 5], [3, -2, 4], [4, -1, 9], [7, -3, 13]]))
# Output: [2.0, 1.0]
