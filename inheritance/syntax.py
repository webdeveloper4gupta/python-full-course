# here i will tell you single inheritance
class aman:
    a=90
    def func1(self):
        print("aman class function")
    def func3(self):
        print(self.a)

class sukritan(aman):
    b=89
    def func2(self):
        print("sukritan class function")

a=aman()
b=sukritan()
b.func1()
b.a=89#istanse attribute change
# a.func2(gives error)
b.func2()
b.func3()
a.func3()