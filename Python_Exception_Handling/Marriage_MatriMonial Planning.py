import user_Defined_Exception
age=int(input("Enter your Age"))
try:
    if age>60:
        raise user_Defined_Exception.Too_Young_Exception("Please Wait For Some More Year you will definately getting the Match")
    elif age<18:
        raise user_Defined_Exception.Too_Old_Exception("You are Too Late Now No Scopes for you ")
    else:
        print("You will get the Match Details through Email ")
except user_Defined_Exception.Too_Young_Exception as e:
    print(e)
except user_Defined_Exception.Too_Old_Exception as e:
    print(e)