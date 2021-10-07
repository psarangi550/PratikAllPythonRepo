# list1=[(i,j)for i in "abcd" for j in "0123" ]
# print(list1)

# # help(zip())
import itertools
# result=itertools.cycle([1,2,3,4])
# print(next(result))
# print(next(result))
# print(next(result))
# # print(next(result))
# # print(next(result))
#
# l1=map(pow,range(1,5),itertools.repeat(2))
# print(list(l1))


# l1=itertools.starmap(pow,[(1,2),(2,3)])
# print(list(l1))

# print(dir(itertools))

# l1=itertools.islice(range(1,10),5)
# for l in l1:
#     print(l)


# import operator
# l1=itertools.accumulate(range(1,5),operator.mul)
# for l in l1:
#     print(l)


# #dictionary comprehension
# name=["Bruce","Clark","Peter","logan","wade"]
# superhero=["Batman","Superman","Spiderman","wolverin","deadpool"]
# d={ k:v for k,v in zip(name,superhero) if k!="Peter"}
# print(d)

#set Comprehension
# nums=[1,1,2,1,3,4,5,5,6,7,8,7,9,9]
# s={n for n in nums}
# print(s)

#generator comprehension
l1=[1, 2, 3, 4, 5, 6, 7, 8, 9]
g=(n*n for n in l1)
# for gen in g:
#     print(gen)