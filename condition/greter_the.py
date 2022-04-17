# here i find greater then four element
a=int(input("enter the number "))
b=int(input("enter the number"))
c=int(input("enter the number"))
d=int(input("enter thenumber"))
if a>b and b>c and c>d:
    print(a)
elif b>a and a>c and c>d:
    print(b)
elif c>a and a>b and b>d:
    print(c)
else:
    print(d)