def find_treasure(matrix, treasure):
	for row in range(len(matrix)):
		for col in range(len(matrix)):
			if matrix[row][col] == treasure:
				return [row, col]
	return [-1, -1]

rooms = [
    [1, 4, 7, 11],
    [8, 9, 10, 20],
    [11, 12, 17, 30],
    [18, 21, 23, 40]
]

print(find_treasure(rooms, 17))
print(find_treasure(rooms, 5))
