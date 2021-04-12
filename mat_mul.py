def mat_mul(x, y):
    rows= len(x)
    cols = len(y[0])
    matrix = [[0 for a in range(cols)] for b in range(rows)]

    for i in range(rows):
        for j in range(cols):
            for k in range(len(y)):
                matrix[i][j]+= x[i][k] * y[k][j]
    for m in matrix:
        print(m)


mat_mul([[1, 2], [3, 4], [5, 6], [7, 8]], [[9, 10, 11], [12, 13, 14]])