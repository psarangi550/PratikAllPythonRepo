class Too_Young_Exception(Exception):
    def __init__(self,message):#constructor with Parameter as message which is the description
        self.message=message #intializing the instance variable
        #here we need to put any message we can put it through using the message
    def __str__(self):#defining the __str__() magic method to customize the exception description
        return "Please Wait For Some More Year you will definately getting the Match"
class Too_Old_Exception (Exception):
    def __init__(self,message):#constructor with Parameter as message which is the description
        self.message=message #intializing the instance variable
        #here we need to put any message we can put it through using the message
    def __str__(self):#defining the __str__() magic method to customize the exception description
        return "You are Too Late Now No Scopes for you  "
