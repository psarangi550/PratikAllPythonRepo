import itertools

f=open("abc.txt","r")

it=itertools.islice(f,0,3)

for i in it:
    print(i)