class P(object):
    def __init__(self):
        print("Parent class Constructor")
    def m1(self):
        print("Parent class Instance method")
class C(P):
    @classmethod
    def m2(cls):
        super(C,cls).__init__(cls)
        super(C,cls).m1(cls)

C.m2()



