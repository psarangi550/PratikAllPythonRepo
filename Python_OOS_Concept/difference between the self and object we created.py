class test:
    def __init__(self,name,age,mark):
        self.name=name
        self.age=age
        self.mark=mark
        print(f"Addess of self is {id(self)}")
    def talk(self):
        print(f"hello my name is {self.name}")
        print(f"my age is{self.age}")
        print(f"and marks are {self.mark}")
t1=test("pratik",40,78)
t2=test("rika",24,98)
print(id(t1))
print(id(t2))