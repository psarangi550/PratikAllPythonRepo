class sentence(object):
    def __init__(self, string_value):
        self.string_value = string_value

    def __iter__(self):
        return self
    def __next__(self):
        self.splitter_str_list = self.string_value.split(" ")
        self.split_itr=iter(self.splitter_str_list)
        count=0
        while True:
            if count > len(self.splitter_str_list):
                raise StopIteration
            else:
                print(next(self.split_itr))
            count = count + 1

s = sentence("My Name is Prateek")
for s1 in s:
    print(s1)

