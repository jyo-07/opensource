n = int(input().strip())
s = -1 if n < 0 else 1
n *= s
r = int(str(n)[::-1]) * s
if r < -2 ** 31 or r > 2 ** 31 - 1:
    r = 0
print(r)
