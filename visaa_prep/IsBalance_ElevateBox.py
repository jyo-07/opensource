n = int(input().strip())
a = list(map(int, input().strip().split()))
b = []
for i in range(n):
    l = sum(a[:i])
    r = sum(a[i + 1:])
    bal = abs(l - r)
    b. append(bal)
print(" ".join(map(str, b)))
