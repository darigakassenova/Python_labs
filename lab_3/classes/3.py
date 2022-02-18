class Shape():
    def _init_(self,lenght,width):
        self.lenght=int(input())
        self.width=int(input())
    def area(self):
        print(self.lenght*self.width)
class Rectangle(Shape):
    def _init_(self,lenght,width):
        Shape._init_(self,lenght,width)
x = Rectangle(Shape)
x.area()