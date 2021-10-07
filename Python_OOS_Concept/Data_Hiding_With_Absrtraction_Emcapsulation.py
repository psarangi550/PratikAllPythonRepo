#here we are taking the example of account Balance into the picture
#we want outside not be able to create the object of account with balance status
#we can mentioned that in a private member and and hide it under the instance method with some validation
#here the customer can't create the object directly but he has to invoke the instance method where validation already applied

class Account:
    def __init__(self,balance):#constructor
        self.__balance=balance#declaring the balance as private member so that it can only access in the class but not outside the class
    #here we also defined the instance method with validation onc e the validation successful then only it can able to access the instance variable balance
    def get_balance(self):#as its using the instance variable this is instance method
        name=input("Enter the Username")
        password=input("Enter the Password")
        if name=="pratik" and password=="1399":
            print(self.__balance)#accessing the private member
        else:
            print("invalid user ID")
    #same we can provide the validation for the deposit and withdrawal method
    def deposite(self,amount):#instance method with validation
        name=input("Enter the Username")
        password=input("Enter the Password")
        if name=="pratik" and password=="1399":
            self.__balance=self.__balance+int(amount)
            print(self.__balance)#accessing the private member
        else:
            print("invalid user ID")

    def withdraw(self, amount):  # instance method with validation
        name = input("Enter the Username")
        password = input("Enter the Password")
        if name == "pratik" and password == "1399":
            if self.__balance<int(amount):
                print("insufficient funds")
            else:
                self.__balance=self.__balance-int(amount)
                self.get_balance()#calling the getBalcance instance method
        else:
            print("invalid user ID")

#now here customer try to create the object
a=Account(1000)#creating the object passing the value of the instance variable
# print(a.balance)#here if the person try to access the value then it will get error as the balance is a private instance method
#but it can access by using the pubkic method where validation already applied
a.get_balance()#callinng the instance method to acces sht epriovate member with validation
amount=input("Enter the Amount to deposite")
a.deposite(amount)
withdraw=input("Enter the Amount to withdraw")
a.withdraw(withdraw)

