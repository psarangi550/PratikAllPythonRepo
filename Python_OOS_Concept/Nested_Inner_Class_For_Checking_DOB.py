class Human:
    def __init__(self,name,date,month,year):
        self.name=name
        self.dob=self.DOB(date,month,year)
    def info(self):
        print(f"Hello, {self.name}")
        self.dob.display()
    class DOB:
        def __init__(self,date,month,year):
            self.date=date
            self.month=month
            self.year=year
        def display(self):
            print(f"Date Of Birth is {self.date}:{self.month}:{self.year}")
name=input("Enter your Name")
date=input("Enter a Date of DOB")
month=input("Enter the Month of the DOB")
year=input("Enter the Year of the DOB")
h=Human(name,date,month,year)
h.info()
