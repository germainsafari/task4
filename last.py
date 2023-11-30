def SystemSolve(matrix):
    # Check if the matrix is empty
    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    # Check for inconsistent system (more variables than equations)
    if cols - 1 > rows:
        return []

    for i in range(rows):
        # Find pivot for this column
        pivot_row = i
        for j in range(i + 1, rows):
            if abs(matrix[j][i]) > abs(matrix[pivot_row][i]):
                pivot_row = j

        # Swap the rows for partial pivoting
        matrix[i], matrix[pivot_row] = matrix[pivot_row], matrix[i]

        # Check if the system is inconsistent
        if matrix[i][i] == 0:
            return []

        # Normalize the pivot row
        pivot_value = matrix[i][i]
        for j in range(cols):
            matrix[i][j] /= pivot_value

        # Eliminate other rows
        for k in range(rows):
            if k != i:
                factor = matrix[k][i]
                for j in range(cols):
                    matrix[k][j] -= factor * matrix[i][j]

    # Check for inconsistent system (non-empty row with all zeros in the coefficients)
    for i in range(rows):
        if all(coeff == 0 for coeff in matrix[i][:-1]) and matrix[i][-1] != 0:
            return []

    # Extract the solutions
    solutions = [row[-1] for row in matrix]

    return solutions[:-1] if len(solutions) == cols else solutions

# Examples
print(SystemSolve([[0, 4, 2, -2], [-2, 3, 1, -7], [4, 5, 2, 4]]))
# Output: [2, -2, 3]

print(SystemSolve([[1, 3, 5], [2, 6, 5]]))
# Output: []

print(SystemSolve([[1, 3, 5], [3, -2, 4], [4, -1, 9], [7, -3, 13]]))
# Output: [2, 1]
