#here we are considering the > and < along with >= and <= and == and != operator on the student object
#method=========================>Magic Method
#> it is =======================>__gt__()
#< it is =======================>__lt__()
#<= it is =======================>__le__()
#== it is =======================>__eq__()
#!= it is =======================>__ne__()

#if we execute __gt__() automatically __lt__() will be execute by the pvm but not __le__() or __ge__()
#if we execute __ge__() automatically __le__() will be execute by the pvm but not __lt__() or__gt__()
#if we execute __eq__() automatically __ne__() will also execute only

class student:
    def __init__(self,mark):
        self.mark=mark
    def __gt__(self, other):#magic method
        if self.mark>other.mark:
            return student(self.mark)
            # return True
        else:
            return student(other.mark)
            # return False
    # def __lt__(self, other):  # magic method
    #     if self.mark <= other.mark:
    #         return (self.mark)
    #     else:
    #         return (other.mark)
    def __str__(self):
            return(f'The lowest Mark value is {self.mark}')
s1=student(56)
s2=student(98)
print(s2>s1)
print(s1<s2)



