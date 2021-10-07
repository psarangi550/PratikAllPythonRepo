class student:
    school_name="Tangi Vidyapitha"
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    @classmethod
    def m1(cls,mark):
        cls.school_name="DRIEMS"
        print(f"school name is {cls.school_name}")
        cls.mark=mark
    @classmethod
    def display(cls):
        print(f"Everyone Mark is {cls.mark}")
        print(f"Everyone school is  {cls.school_name}")
    def info(self):
        print(f"name: {self.name}")
        print(f"name: {self.rollno}")
    @staticmethod
    def add(a,b):
        return(a+b);
s=student("pratik",101)
s.info()
student.m1(90)
# s.m1()
result=student.add(10,20)
print(result)
print(s.add(10,20))
student.display()
