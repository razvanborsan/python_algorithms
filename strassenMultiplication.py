
import numpy as np


def split_matrix(mat):
    size = len(mat)
    middle = size // 2

    top_left = np.matrix([[mat[i][j] for j in range(middle)] for i in range(middle)])
    top_right = np.matrix([[mat[i][j] for j in range(middle, size)] for i in range(middle)])
    bottom_left = np.matrix([[mat[i][j] for j in range(middle)] for i in range(middle, size)])
    bottom_right = np.matrix([[mat[i][j] for j in range(middle, size)] for i in range(middle, size)])

    return top_left, top_right, bottom_left, bottom_right


def strassen(mat_x, mat_y):
    if len(mat_x) == 1:
        return mat_x[0][0] * mat_y[0][0]

    a, b, c, d = split_matrix(mat_x)
    e, f, g, h = split_matrix(mat_y)

    p1 = strassen(a, f - h)
    p2 = strassen(a + b, h)
    p3 = strassen(c + d, e)
    p4 = strassen(d, g - e)
    p5 = strassen(a + d, e + h)
    p6 = strassen(b - d, g + h)
    p7 = strassen(a - c, e + f)

    top_left = p5 + p4 - p2 + p6
    top_right = p1 + p2
    bot_left = p3 + p4
    bot_right = p1 + p5 - p3 - p7

    new_matrix = np.vstack([np.hstack([top_left, top_right]), np.hstack([bot_left, bot_right])])
    return np.matrix(new_matrix)
