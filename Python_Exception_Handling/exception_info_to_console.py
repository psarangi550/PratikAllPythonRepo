try:#try block with riskey code
    x=input("Enter the first Number")
    y=input("Enter the 2nd Number")
    print(int(x)/int(y))#riskey code
except (ZeroDivisionError ,ValueError) as e:#handling code inside the except method
    #here we want to display 3 things 1 st is the type 2nd is the Name and third is the description
    #going for the first :-Showing the type in here
    print(f"The Type Of Exception is {type(e)}")
    print(f"The Type Of Exception is {e.__class__}")
    #going for Name 2nd thing i.e the name of the exception only
    print(f"The Name Of Exception is {e.__class__.__name__}")
    #going for displaying the total description which has been written by the __str__() as in here we are trying to print the object reference of
    #zeroDivisionError object reference which is nothing but e so as we are tryting to print the object reference hence
    #corresponding __magic__method i.e __str__()is going to get executed
    print(f"Exception Description is {e}")
# except ValueError  as e:#handling code inside the except method
#     #here we want to display 3 things 1 st is the type 2nd is the Name and third is the description
#     #going for the first :-Showing the type in here
#     print(f"The Type Of Exception is {type(e)}")
#     print(f"The Type Of Exception is {e.__class__}")
#     #going for Name 2nd thing i.e the name of the exception only
#     print(f"The Name Of Exception is {e.__class__.__name__}")
#     #going for displaying the total description which has been written by the __str__() as in here we are trying to print the object reference of
#     #zeroDivisionError object reference which is nothing but e so as we are tryting to print the object reference hence
#     #corresponding __magic__method i.e __str__()is going to get executed
#     print(f"Exception Description is {e}")