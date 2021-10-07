#if an Object can walk like a duck and quack like a duck then its considered to be duck
#whether its actually a duck or not it does not matter
#as long as it has the walk and quack same as duck object then its considered as duck object only

#in python behaviour gets more priority than the type
#But in other languages Type get more priority than the Behaviour
#let take this example

class duck:
    def quack(self):
        print("Quack Quack....")
class Monkey:
    pass
    # def quack(self):
    #     print("Monkey acting link Duck and saying Quack and Quack")
#for Non-Pythonic Approach then
#check the type first if the type matched then as for behavior


# def invoke_quack(object):#for calling the class quack method by taking the object as argument
#     #for Non-Pythonic approach check the typ[e then ask for behaviour
#     # if isinstance(object,duck):
#     #     object.quack()
#     # else:
#     #     print("for invoking the Quack method object should be of duck type")
#     #pythonic approach is
#     object.quack()
#

#with LBYL:-non pythonic qappriach
# def invoke_quack(object):
#    if isinstance(object,duck):
#        if hasattr(object, "quack"):
#            if callable(object.quack()):
#                object.quack()
#            else:
#                pass


#with EAFP:-
def invoke_quack(object):
    try:
        object.quack()
    except AttributeError as e:
        print(e)


d=duck()#creating the object of duck class
m=Monkey()#creating the object of monkey class

#now we want to call the invoke _quack method passing the object as args
invoke_quack(d)#calling the method by passing duck object
invoke_quack(m)#calling the method by passing the monkey object

#o/p-:-Quack Quack....
# for invoking the Quack method object should be of duck type

#o/p by pythonic approach
# Quack Quack....
# Monkey acting link Duck and saying Quack and Quack
#here we can ask for forgiveness by the try except method