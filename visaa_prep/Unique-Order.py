n = int(input().strip())
arr = list(map(int, input().split()))
s = set()
a = []
               
for i in arr:
    if i not in s:
        s.add(i)
        a.append(i)
print(' '.join(map(str, a)))
