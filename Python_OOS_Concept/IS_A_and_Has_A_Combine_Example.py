# #1st Approach
# class Car:
#     def __init__(self,model,color,price):
#         self.model=model
#         self.color=color
#         self.price=price
#     def car_info(self):
#         print(f"MODEL:{self.model} \n COLOR:{self.color} \n PRICE:{self.price} ")
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def person_info(self):
#         print(f"Name:{self.name} \n AGE: {self.age}")
# class Employee(Person):
#     def __init__(self,name,age,eno,esal,model,color,price):
#         super().__init__(name,age)
#         self.eno=eno
#         self.esal=esal
#         self.car=Car(model,color,price)
#     def display(self):
#         print(f"EMP NO: {self.eno}\n EMP SAL: {self.esal}")
#         print("Car info")
#         self.car.car_info()
#         print()
#         print("Person Details")
#         self.person_info()
#         super().person_info()
#         print()
#         print("Employee Info")
#         print(f"EMP NO:{self.eno} \n EMP SAL: {self.esal}")
# e=Employee("pratik",40,101,10000,"Audi","Silver","1000000")
# e.display()

#2nd Approach:-
###################

class Car:
    def __init__(self,model,color,price):
        self.model=model
        self.color=color
        self.price=price
    def carInfo(self):
        print(f"MODEL:{self.model}\nCOLOR:{self.color}\n{self.price}")
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def person_Info(self):
        print(f"NAME:{self.name}\nAGE:{self.age}")
class Employee(Person):
    def __init__(self,name,age,eno,esal,car):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal
        self.car=car
    def display(self):
        print("CAR DETAILS")
        self.car.carInfo()
        print()
        print("PERSON DETAILS")
        self.person_Info()
        # super().person_Info
        print()
        print("EMPLOYEE DETAILS")
        print(f"EMP NO: {self.eno}\nEMP SALARY: {self.esal}")

c=Car("Audi","Brown",1000000)
emp=Employee("pratik",40,101,10000,c)
emp.display()
