class remote:
    def isLeftPressed(self):
        return True
    

class game:
    def moveleft(self):
        print('now i am moving to left')
    def moveright(self):
        print("now i am moving to right")
aman=remote()
aman1=game()
if(aman.isLeftPressed()):
    aman1.moveleft()