#in case of multiple inheritance one class can in herit from multiple classes
#but in the same also the order of the classes described does matter the most
#PVN will always check first in the same class whether the same method being present or not
#if the same method being present then it will consider the child class method first
#if not the order in which parent class described matters the most
#pvm will 1st check the parent classs from left to right if fount it wil;l not check in the next parent if not found then
# only it will traver the next parent class
class p1:#parent class  p1
    def m1(self):#instance method
        print("P1 parent class m1 method ")
class p2:
    def m1(self):
        print("P2 parent class m1 method")
#case:-1
#=========
# class C(p1,p2):#extending from the both parent multiple inheritance
#     def m1(self):
#         print("Child class m1 method ")
# c=C()#creating the object and executing the constructor
# c.m1()#calling the instance method

# #case:-2
# #=========
# class C(p1,p2):
#     def m2(self):
#         print("P2 parent class m1 method")
# c=C()#creating the child class object and executing the constructor
# c.m1()#calling the parent class instance method from the child class object

#case:3
#========
class C(p2,p1):
    def m2(self):
        print("P2 parent class m1 method")
c=C()#creating the child class object and executing the constructor
c.m1()#calling the parent class instance method from the child class obje