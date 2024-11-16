x = int(input())
Spring = [3, 4, 5]
Summer = [6, 7, 8]
Autumn = [9, 10, 11]
Winter = [12, 1, 2]
if(x > 12):
    print("Invalid")
elif(x in Spring):
    print("Spring")
elif(x in Summer):
    print("Summer")
elif(x in Autumn):
    print("Autumn")
else:
    print("Winter")
