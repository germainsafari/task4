def SystemSolve(matrix):
    # Function to perform Gaussian elimination
    def gauss_elimination(matrix):
        rows, cols = len(matrix), len(matrix[0])

        for i in range(min(rows, cols - 1)):
            # Make the diagonal element 1
            diagonal_element = matrix[i][i]
            if diagonal_element == 0:
                # Swap rows to make diagonal element non-zero
                for k in range(i + 1, rows):
                    if matrix[k][i] != 0:
                        matrix[i], matrix[k] = matrix[k], matrix[i]
                        break

            diagonal_element = matrix[i][i]

            if diagonal_element == 0:
                continue

            for j in range(cols):
                matrix[i][j] /= diagonal_element

            # Make the elements below the diagonal zero
            for k in range(i + 1, rows):
                factor = matrix[k][i]
                for j in range(cols):
                    matrix[k][j] -= factor * matrix[i][j]

    # Perform back-substitution to find solutions
    def back_substitution(matrix):
        rows, cols = len(matrix), len(matrix[0])
        solutions = [0] * min(rows, cols - 1)

        for i in range(min(rows, cols - 1) - 1, -1, -1):
            solutions[i] = matrix[i][cols - 1]
            for j in range(i + 1, cols - 1):
                solutions[i] -= matrix[i][j] * solutions[j]

        return solutions

    # Copy the matrix to avoid modifying the input
    augmented_matrix = [row[:] for row in matrix]

    # Perform Gaussian elimination
    gauss_elimination(augmented_matrix)

    # Check for inconsistent or infinite solutions
    for row in augmented_matrix:
        if row[:-1] == [0] * (len(row) - 1) and row[-1] != 0:
            # Inconsistent solution
            return []

    # Perform back-substitution
    solutions = back_substitution(augmented_matrix)

    return solutions

# Test cases
# print(SystemSolve([[0, 4, 2, -2], [-2, 3, 1, -7], [4, 5, 2, 4]]))  # Consistent solution: [2, -2, 3]
# print(SystemSolve([[1, 3, 5], [2, 6, 5]]))  # Inconsistent solution: []
# # Output: [2.0, 1.0]
# print(SystemSolve([[3, 1, -1, 1], [1, -1, 1, -3], [2, 1, 1, 0]]))
# # output: [-0.5000000000000002, 1.7500000000000004, -0.7500000000000001]
# # ex
# print(SystemSolve([[-1, -2, 1, -1], [2, 3, 0, 2], [0, 1, -2, 0]]))
# # output: [1.0, 0.0]
print(SystemSolve([[0, 4, 2, -2], [-2, 3, 1, -7], [4, 5, 2, 4]]))
# Output: [2.0, -2.0, 3.0]

print(SystemSolve([[1, 3, 5], [2, 6, 5]]))
# Output: []

print(SystemSolve([[1, 3, 5], [3, -2, 4], [4, -1, 9], [7, -3, 13]]))
# Output: [2.0, 1.0]
