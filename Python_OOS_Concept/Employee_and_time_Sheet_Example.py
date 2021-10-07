class Employee:
    def __init__(self,name, wedges):
        self.name=name
        self.wedges=wedges
    # def __mul__(self, other):
    #     return(self.wedges*other.no_of_days)
class Timesheet:
    def __init__(self,name,no_of_days):
        self.name=name
        self.no_of_days=no_of_days
    def __mul__(self, other):
        return(self.no_of_days*other.wedges)
e=Employee("Pratik",500)
t=Timesheet("Pratik",22)
# print(e*t)
print(t*e)
