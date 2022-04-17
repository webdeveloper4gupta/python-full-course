def aman(num):
    try:
        return int(num)+1
    except:
        raise ValueError("value error comes")
a=aman("sukritan")
print(a)