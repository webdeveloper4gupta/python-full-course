class aman:
    num1=0
    
    def __init__(self,num1):
        self.num1=num1
        
    def  __add__(self,num):
        return self.num1+num.num1

a=aman(1)
b=aman(2)
c=a+b
print(c)
