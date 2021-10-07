import inspect #importing the inspect module
def get_info():#get_info method
    print(inspect.stack()[1][3])#calling the Stack function in order to get the stack trace from where the request came in
    print(inspect.stack()[1][1])#calling the Stack function in order to get the stack trace from where the request came in
