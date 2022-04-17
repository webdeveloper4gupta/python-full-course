class c1:
    def __init__(self):
   
        print("constructor of c1 class")

class c2(c1):
    def __init__(self):
        super().__init__()#used to call constructor ofbase class
        print("constructor of c2 class")

a=c2()
