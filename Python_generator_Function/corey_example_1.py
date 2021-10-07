class my_range(object):
    def __init__(self,start,end):
        self.start=start
        self.end=end
    def __iter__(self):
        return self
    def __next__(self):
        if self.start>=self.end:
            raise StopIteration
        else:
            self.start+=1
            return self.start
my_obj=my_range(10,20)
for x in my_obj:
    print(x)

