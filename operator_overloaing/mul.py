class aman:
    n=0
    def __init__(self,n1):
        self.n=n1
    def __mul__(self,n1):
        return self.n*n1.n     

a=aman(3)
b=aman(10)
c=a*b
print(c)