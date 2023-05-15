matrix = [[3, 7, 9],
          [4, 2, 6],
          [8, 1, 5]]
trails = []

for r in range(3):
    for c in range(3):
        trails.append(matrix[r][c])
print(trails)

zipped_matrix = list(zip(*matrix))
print(zipped_matrix)
transported_matrix = list(map(list, zip(*matrix)))
print(transported_matrix)