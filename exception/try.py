a=int(input("enter the number according to your wish \n"))
b=int(input("enter the umbewr according to your wish \n"))
try:
    c=a/b
    print(c)
except Exception as e:
    print('error comes')
    print(e)