class aman:
    n=0
    def __init__(self,n1):
        self.n=n1
    def __floordiv__(self,n1):
        return self.n // n1.n
    
a=aman(11)
b=aman(2)
c=a//b
print(c)