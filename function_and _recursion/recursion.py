def aman(n):
    if n!=0:
        return aman(n-1)+n
    else:
        return 0

c=aman(10)
print(c)