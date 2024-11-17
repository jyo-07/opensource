x = int(input().strip())
for _ in range(x):
    a, b = map(int, input().split())
    points = a // 10
    score = points * b
    print(score)
