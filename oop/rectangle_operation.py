class aman:
    length=0
    breadth=0
    def get(self):
        self.length=int(input("enter the length of rectangle"))
        self.breadth=int(input("enter the breadth of rectangle"))
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)

object =aman()
object.get()
area=object.area()
perimeter=object.perimeter()
print(f"the area of rectangle is {area}")
print(f"the perimeter of rectangle is{perimeter}")