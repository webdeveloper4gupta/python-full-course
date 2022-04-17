class aman:
    a=90
    def func(self):
        print(self.a)
a=aman()
a.a=9000#it changes only the value of a of aman object not for class
a.func()