class customer:
    '''This is a cutomer class just to perform deposite and withdraw operation'''
    bank_name="Code_with_Pratik Bank"
    def __init__(self,name,balance=0.0):#constructor with parameter
        self.name=name#declaring and initializing the instance variable
        self.balance=balance#declaring and initializing the instance variable
    def Desposite(self,amount):#instance method
        self.balance=self.balance+amount
        print(f"your account Balance is {self.balance}")
    def withdrawal(self,amount):#instance method
        if(amount>self.balance):
            print("your account does not have sufficient Balance to withdraw")
        else:
            self.balance = self.balance-amount
            print(f"your account Balance is {self.balance}")

#the above one is class declaration
#now stats the declaration
print(f"Welcome to {customer.bank_name} ")
name = input("Please Enter a Name")
c = customer(name)  # creating the object of customer class object and executing the constructor
while True:
       option=input("Which Operation you want to Perform \n D:-Deposite \n W-withdrawal")
       if(option.lower()=="d"):
           amount=float(input("Enter the Amount you want to Deposite"))
           c.Desposite(amount)
       elif(option.lower()=="w"):
           cash=float(input("Enter the Amount you want to withdraw"))
           c.withdrawal(cash)
       else:
           print("Invalid Option chosen")

