import time
import importlib
import cehcking_Module_Reloading_1#importing the module
print(cehcking_Module_Reloading_1.add(10,20))
time.sleep(50)#sleeping the program 50 seconds
importlib.reload(cehcking_Module_Reloading_1)
print(cehcking_Module_Reloading_1.product(10,20))