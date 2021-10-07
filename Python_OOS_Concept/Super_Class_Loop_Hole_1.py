class A:
    def __init__(self):
        print("Parent class  A Constructor")

class B(A):
    def __init__(self):
        print("Parent class  B Constructor")
    def m1(self):
        print("M1 Method")

class C(B):
    def __init__(self):
        print("Parent class  C Constructor")


class D(C):
    def __init__(self):
        print("Parent class  D Constructor")

class E(D):
   def m2(self):
       B.m1(self)
       super(C,self).m1()
       B.__init__(self)
       super(C,self).__init__()


e=E()#creating the class for E Object
e.m2()