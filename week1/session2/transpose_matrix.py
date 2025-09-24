
def transpose(matrix):
    # optimal example
    return [list(new_row) for new_row in zip(*matrix)]

    # matrix can be any dimensions
    # row = len(matrix)
    # col = len(matrix[0])
    # result_matrix = [[0 for i in range(row)] for j in range(col)]
    # print(result_matrix)

    # for i in range(0,row):
    #     for j in range(0,col):
    #         result_matrix[j][i] = matrix[i][j]

    # return result_matrix

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(transpose(matrix))

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(transpose(matrix))