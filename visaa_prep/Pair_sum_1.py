N = int(input().strip())
arr = list(map(int, input().split()))
k = int(input().strip())
c = set()
f = False
for num in arr:
    if k - num in c:
        f = True
        break
    c.add(num)
print("true" if f else "false")
