# import collections
from collections.abc import Hashable
l=[10,20,40]
t=(10,20,30,40,50)
print(isinstance(l,Hashable))
print(isinstance(t,Hashable))
#if we want to know the hash code we can use the method hash()
print(hash(t))#value will come
print(hash(l))#here in this case we will get the type Error