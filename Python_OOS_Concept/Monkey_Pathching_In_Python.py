#changing the Attribute of a class dynamically at the runtime is called Monkey Patching
#its a common nature for dynamically typed Language
#lets suppose below example
class Test:#class Test
    def __init__(self):#constructor
        pass#nothing to initialize
    def fetch_Data(self):#instance method
        #remeber that function is also a object and function name is the variable which been pointing to the function object that
        #that means:-function object has some id and function name variable pointing to that function object
        #address of function object and function reference variable being same as of now
        print("lets suppose its been fetching the data from DB")
        #after this  data Fetched from DB we want to perform some activity using another function
    def f1(self):#instance method
        self.fetch_Data()#calling the  instance method
#now  we realized that we should not deal with the live DB but we have to pre store test dat with which we need to test
#which is
def fetch_new_data(x):#here we are taking x as args as it will replace the ond live DB Data and we know self is not a keyword hence we cantake any args and PVM will provide the value for the same
    print("lets suppose its been fetching the data from Test DB")
#so we can change the data fetching from the old DB to the New DB Using the Monkey Patching at runtime
#we can write as below:-
Test.fetch_Data=fetch_new_data
#here the fetch_new_data function object referred by variable fetch_new_data same like fetch_data
#as function is the object and which is referred by the function reference variable
#here you can see we are not calling the method we are assigning the reference variable fetch_new_data reference to
# fetch data reference
#now the fetch_data is now not refer its old function object but its now pointing to the new function object as we assign the fetch_new_Data reference variable to fetch_data
#now if we try to access the fetch_data it will provide the new Fetch_new_Data info
Test().fetch_Data()#creating Test class Object and calling the instance method

#lets suppose its been fetching the data from Test DB

