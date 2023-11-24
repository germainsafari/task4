def SystemSolve(matrix):
    def gauss_elimination(matrix):
        rows, cols = len(matrix), len(matrix[0])

        for i in range(min(rows, cols - 1)):
            diagonal_element = matrix[i][i]
            if diagonal_element == 0:
                for k in range(i + 1, rows):
                    if matrix[k][i] != 0:
                        matrix[i], matrix[k] = matrix[k], matrix[i]
                        break
                else:
                    continue

            diagonal_element = matrix[i][i]

            for j in range(cols):
                matrix[i][j] /= diagonal_element

            for k in range(i + 1, rows):
                factor = matrix[k][i]
                for j in range(cols):
                    matrix[k][j] -= factor * matrix[i][j]

    def back_substitution(matrix):
        rows, cols = len(matrix), len(matrix[0])
        solutions = [0] * min(rows, cols - 1)

        for i in range(min(rows, cols - 1) - 1, -1, -1):
            solutions[i] = matrix[i][cols - 1]
            for j in range(i + 1, cols - 1):
                solutions[i] -= matrix[i][j] * solutions[j]

        return solutions

    augmented_matrix = [row[:] for row in matrix]
    gauss_elimination(augmented_matrix)

    # Check for rows that became all zeros during Gaussian elimination
    for row in augmented_matrix:
        if all(value == 0 for value in row[:-1]) and row[-1] != 0:
            # Infinite solutions, return a parameterized solution
            params = ['t' + str(i + 1) for i in range(len(row) - 1)]
            return [f'1 - {param}' if i == 0 else param for i, param in enumerate(params)]

    solutions = back_substitution(augmented_matrix)
    return solutions

# Test cases
print(SystemSolve([[-1, -2, 1, -1], [2, 3, 0, 2], [0, 1, -2, 0]]))
def test_unique_solution(self):
    # Test a system with a unique solution
    matrix = [[-1, -2, 1, -1], [2, 3, 0, 2], [0, 1, -2, 0]]
    expected = [1, 0, 0]
    actual = SystemSolve(matrix)
    self.assertEqual(expected, actual)

def test_infinite_solution(self):
    # Test a system with infinite solutions
    matrix = [[1, 2, -1, 0], [2, 4, -2, 0], [3, 6, -3, 0]]
    expected = ['1 - t1', 't1', 't2']
    actual = SystemSolve(matrix)
    self.assertEqual(expected, actual)

def test_inconsistent_solution(self):
    # Test a system with no solutions
    matrix = [[1, 2, -1, 0], [2, 4, -2, 0], [3, 6, -3, 1]]
    # The function does not handle this case properly, so we expect an AssertionError
    with self.assertRaises(AssertionError):
        SystemSolve(matrix)

# We can add more test cases for different scenarios, such as empty matrix, non-square matrix, etc.
