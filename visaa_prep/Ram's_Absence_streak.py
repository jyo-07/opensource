N = int(input().strip())
a = list(map(int, input().split()))
current = 0
m = 0
for i in a:
    if i == 0:
        current += 1
        if current > m:
            m = current
    else:
        current = 0
print(m)
