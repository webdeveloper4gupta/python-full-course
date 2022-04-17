class c1:
    def func1(self):
        print("c1 class function")
    
class c2(c1):
    def func2(self):
        super().func1()

class c3(c2):
    def func3(self):
        print("c3 class function")

a=c3()
a.func3()
a.func1()
a.func2()