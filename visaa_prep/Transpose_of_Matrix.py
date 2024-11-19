N = int(input().strip())
matrix = []
for _ in range(N):
    row = list(map(int, input().strip().split()))
    matrix.append(row)
t_matrix = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        t_matrix[j][i] = matrix[i][j]
for row in t_matrix:
    print(' '.join(map(str, row)))
