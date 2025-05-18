from typing import List

def matrix_multiply(matrix1: List[List[int]], matrix2: List[List[int]]) -> List[List[int]]:
    """
    Множення двох матриць.

    :param matrix1: Перша матриця (розмір m x n)
    :param matrix2: Друга матриця (розмір n x p)
    :return: Результат множення матриць (розмір m x p)

    Приклад:
    >>> A = [[1, 2, 3],
    ...      [4, 5, 6]]
    >>> B = [[7, 8],
    ...      [9, 10],
    ...      [11, 12]]
    >>> matrix_multiply(A, B)
    [[58, 64], [139, 154]]

    Приклад множення одиничної матриці:
    >>> I = [[1, 0], [0, 1]]
    >>> M = [[5, 6], [7, 8]]
    >>> matrix_multiply(I, M)
    [[5, 6], [7, 8]]

    Помилка, якщо розміри не сумісні:
    >>> matrix_multiply([[1,2]], [[1,2],[3,4],[5,6]])
    Traceback (most recent call last):
    ...
    ValueError: Матриці не сумісні для множення
    """
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Матриці не сумісні для множення")
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            s = 0
            for k in range(len(matrix2)):
                s += matrix1[i][k] * matrix2[k][j]
            row.append(s)
        result.append(row)
    return result


def transpose_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    Транспонування матриці.

    :param matrix: Матриця розміром m x n
    :return: Транспонована матриця розміром n x m

    Приклад:
    >>> M = [[1, 2, 3],
    ...      [4, 5, 6]]
    >>> transpose_matrix(M)
    [[1, 4], [2, 5], [3, 6]]

    Транспонування квадратичної матриці:
    >>> N = [[1, 2],
    ...      [3, 4]]
    >>> transpose_matrix(N)
    [[1, 3], [2, 4]]

    Транспонування одиничної матриці:
    >>> I = [[1, 0], [0, 1]]
    >>> transpose_matrix(I)
    [[1, 0], [0, 1]]
    """
    return [list(row) for row in zip(*matrix)]

