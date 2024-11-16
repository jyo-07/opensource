a = int(input())
for _ in range(a):
    x, N = map(int, input().split())
    points = (x//10)*N
    print(points)
