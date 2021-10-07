class P:
    a=10#static variable
    def __init__(self):#parent class constructor
        print("Parent class Constructor")
    def m1(self):#instance method
        print("Parent class instance method")
    @classmethod
    def m2(cls):
        print("Parent class method")
    @staticmethod
    def m3():
        print("Parent class staic method ")
class C(P):
    def method1(self):
        print(f"static variable value is ${self.a}")#accessing the static variable of the parent class using the object reference
        print(f"Static variable value is ${P.a}")#calling the parent class static variable by the help of class Name
        super().__init__()#calling the parent class constructor
        self.m1()#calling the parent class instance method
        print("*"*50)#decorating
        #now using the super()
        print(super().a)
        super().m1()
c=C()#creating the child class object and executing the constructor
c.method1()
        