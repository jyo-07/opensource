N = int(input().strip())
matrix = []
for _ in range(N):
    row = list(map(int, input().strip().split()))
    matrix.append(row)
m = [row[::-1] for row in matrix]
for row in m:
    print(' '.join(map(str, row)))
