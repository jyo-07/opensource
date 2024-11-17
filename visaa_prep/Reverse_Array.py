n = int(input().strip())
arr = list(map(int, input().strip().split()))
arr.reverse()
print(" ".join(map(str, arr)))
