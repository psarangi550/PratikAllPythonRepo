
class Book:
    def __init__(self,pages):#constructor to initialize the instance variable
        self.pages=pages
    def __add__(self, other):
        return Book(self.pages+other.pages)
    def __str__(self):
        return(f"The Total Number of pages is {self.pages}")
b1=Book(100)
b2=Book(200)
b3=Book(500)
b=b1+b2
b4=b3+b2
print(b)
print(b4)
