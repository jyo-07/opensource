x = input()
r = []
count = 1
for i in range(1, len(x)):
    if x[i] == x[i-1]:
        count+=1
    else:
        r.append(x[i-1] + str(count))
        count = 1
r.append(x[-1] + str(count))
print(''.join(r))
