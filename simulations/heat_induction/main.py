import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

tempTop = 200
tempBottom = 150
tempLeft = 100
tempRight = 50
plate_width = 40
plate_height = 40


def fill_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            cx = i % plate_width + 1
            cy = i // plate_width + 1
            dx = j % plate_width + 1
            dy = j // plate_width + 1

            del_x = abs(dx - cx)
            del_y = abs(dy - cy)
            if del_x == 1 and cy == dy or del_y == 1 and cx == dx:
                matrix[i][j] = 1

    np.fill_diagonal(matrix, -4)


def get_b(size):
    b = np.zeros(size)
    for i in range(len(b)):
        result = 0
        x = i % plate_width + 1
        y = i // plate_width + 1
        if x == 1:
            result += -tempLeft
        if x == plate_width:
            result += -tempRight
        if y == 1:
            result += -tempTop
        if y == plate_height:
            result += -tempBottom
        b[i] = result

    return b


initial_matrix = np.zeros((plate_height * plate_width, plate_height * plate_width))
fill_matrix(initial_matrix)

inverse_matrix = np.linalg.inv(initial_matrix)

b = get_b(plate_height * plate_width)

result = inverse_matrix.dot(b).reshape((plate_height, plate_width))

ax = sns.heatmap(result, linewidth=0.5)
plt.show()
