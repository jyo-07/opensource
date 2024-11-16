x, y = map(int, input().split())
num_p = (y + 99)//100
if(num_p <= x):
    print("0")
else:
    print(num_p - x)
