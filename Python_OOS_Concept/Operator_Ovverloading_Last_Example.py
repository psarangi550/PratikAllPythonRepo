#here we need to perform multiple operation as
#here i want to built the Operator for the book object to perform this below Operation
#b1+b2*b3+b4
class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self, other):
        print("Addition Operator to just to check which one will execute first")
        return Book(self.pages+self.pages)
    def __mul__(self, other):
        print("Multiplication Operator to just to check which one will execute first")
        return Book(self.pages*other.pages)
    def __str__(self):
        return(f"The Total Result is {self.pages}")
b1=Book(100)
b2=Book(400)
b3=Book(500)
b4=Book(600)
print(b1+b2*b3+b4)
