
class sentence(object):
    def __init__(self,sentence):#constructure
        self.sentence=sentence
        self.index=0
        self.words=self.sentence.split(" ")
    def __iter__(self):
        return self
    def __next__(self):
        # print(self.words)
        if self.index>=len(self.words):
            raise StopIteration
        result=self.words[self.index]
        self.index=self.index+1
        return result
s=sentence("This is a sentence")
for se in s:
    print(se)
