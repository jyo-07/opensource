N = int(input().strip())
for _ in range(N):
    a, b = map(int, input().split())
    runs = a - b + 1
    print(runs)
