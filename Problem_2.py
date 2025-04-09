x = int(input("enter first number"))
y = int(input("enter second number"))
if x - y > 0:
    print(x,"is larger than",y)
elif x - y < 0:
    print(x, "is smaller than", y)
elif x - y == 0:
    print(x, "=", y)