def split_generator(my_string):
    l1=my_string.split()
    i=0
    while i<len(l1):
        yield l1[i]
        i+=1
it=split_generator("My Name is Pratik")
for ele in it:
    print(ele)


