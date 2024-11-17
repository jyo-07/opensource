x = int(input().strip())
for _ in range(x):
    a, b = map(int, input().strip().split())
    if a > b:
        s = a - b
    else:
        s = 0
    print(s)
