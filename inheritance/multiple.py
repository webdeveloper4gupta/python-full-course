class c1:
    def func1(self):
        print("c class function1")
    def func2(self):
        print("c1 class function2")

class c2:
    def func3(self):
        print("c2 class function 3")

class c3(c1,c2):
    def func4(self):
        print("c3 class fun3")

a=c3()
a.func3()    
a.func1()
a.func2()