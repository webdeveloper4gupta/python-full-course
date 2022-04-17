


class sub:
    n1=0
    def __init__(self,n):
        self.n1=n
    def __sub__(self,n):
        return self.n1-n.n1

a=sub(1)
b=sub(2)
c=a-b
print(c)
