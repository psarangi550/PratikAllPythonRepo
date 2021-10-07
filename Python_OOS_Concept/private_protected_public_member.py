# we can access the private member with in the class only but not outside of the class
#we can access th public member with in the class and outside of the class as well
#we can access the protected member with in the class and outside the class with the help of child class
#private member represented by __variable name __method name where constructor also included
#public member :-can be access with in the class out the class as well
#By default all the member of the class i.e. All the variable and method described within the class in public
#protected member can be represented by single underscore symbol like _x and_m

#even though Access Specifier and modifiers are there but that not so much updated in python in language level
#we can access the private member of a class outside class by using name mangling
#name mangling will be performed by pVM
#PVM will change the name of the private member as Below
#__private member= _className__private member
#if we try to access directly then in that case we will get Attribute Error
#but if we try to access the Mangled Name then we can able to access the private  variable outside the class even



#similarly we are able to access the protected method outsiode of the class with out any child class method

#lets see both the examples in here

# class Test:#Test class
#     def __init__(self):
#         self.__x=20#private instance variable
#     def __m1(self):#private instance method
#         print("I am a Private instance method ")
#     #inside the class as we can access the private variable/method we can able to access
#     #here calling the both private instance variable and private instance method inside another instance method
#     def m2(self):#public instance method
#         print(f"{self.__x}")#accessign the private member with in the class which is perfectly fine
#         self.__m1()#calling the private instance method from with in the class
# #creationg the Object for the Test Class
# t =Test()#creating the object of TestClass and executing constructor to initialize the instance variable
# t.m2()#accessing the public instance method from the object
# #here the O/P are:-
# # 20
# # I am a Private instance method
# #but if we are try to access directly we will get Attribute Error
# # t.__m1()#in this case will get Attribute Error  as we are accessing the private instance method
# # print(t.__x)#accessing the private memebr out side the class
# #O/P:-AttributeError: 'Test' object has no attribute '__m1'
#
# #accessing the private member using the Name Mangling concept
# #as described earlier the name of the private variable or method changed as below
# #__private member=_class name__privat member(Ther is No Dot in Between)
# #using this we can access the private class member inside the class
#
# # we need to call this mangled name on the object reference
# print(t._Test__x)
# #similarly checking for the private instance method m1()
# t._Test__m1()
#


#similarly checking for the private access specifier for the protected variable/method/constructor
class Test:#Test Class
    def __init__(self):#constructor
        self._x=30# protected instance variable
    def _m1(self):#protected instance method
        print("Protected instance method")
    def m2(self):#public instance method to access both the protected instance variable and instance method
        self._m1()#accessing the protected member with in the class
        print(self._x)#accessing the protected variable with in the class
class subTest(Test):#child class subTest and Parent class Test
    def m3(self):#public instance method
        self._m1()#calling the Parent class protected member from outside with in the child class
        print(self._x)#accessing and printing the protected variable in here
s=subTest()#creating the object of the subClass
s.m2()#calling the parent class public instance method from the child class object
s.m3()#calling the child class instance method from the child class object
#accessing outside with out any child class method which also work fine
#in Python this Access Modifier and Access Specifier are only for the Good Programming practices
print(s._x)#accessing the parent class protected member outside the class with out child class this al;so works fine
s._m1()#here accessing the protected member outside the class which i think should work fine
