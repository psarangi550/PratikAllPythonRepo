class P:
    @classmethod
    def m1(cls):
        print("Parent class Class Method ")
    @staticmethod
    def m2():
        print("Parent class static method ")
class C(P):
    @staticmethod
    def m3():
        super(C,C).m1()
        super(C,C).m2()
C.m3()