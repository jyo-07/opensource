N = int(input().strip())
count_3 = N//3
count_5 = N//5
count_15 = N//15
res = count_3 + count_5 - count_15
print(res)
