class Employee(object):#employee class
    def __init__(self,first,second,pay):
        self.first=first
        self.second=second
        self.pay=pay
    @property
    def email(self):
        return "{}.{}@gmail.com".format(self.first,self.second)
    @property
    def fullname(self):
        return "{} {}".format(self.first,self.second)
    def __repr__(self):
        return("{},{},{}".format(self.first,self.second,self.pay))

