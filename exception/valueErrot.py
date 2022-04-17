try:
    a=int(input("enter the number"))
    print(a)
except ValueError as e:
    print(e)
    print("error")