from threading import *
def display():
    for i in range(10):
        print("Abi")
t=Thread(target=display,name="Abi")
t.start()
print(enumerate())
print(type(enumerate()))
for i in range(10):
    print("Pratik")

