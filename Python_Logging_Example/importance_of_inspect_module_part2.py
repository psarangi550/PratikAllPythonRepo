#here i am importing the file and calling the functiopn
import importance_of_inspect_module_part1
def m1():#m1 method
    importance_of_inspect_module_part1.get_info()
m1()

# [FrameInfo(frame=<frame at 0x00EB5DA8, file 'C:\\Users\\611903295\\Downloads\\python\\Django_Python_Revesion\\Python_Logging_Example\\importance_of_inspect_module_part1.py', line 3, code get_info>, filename='C:\\Users\\611903295\\Downloads\\python\\Django_Python_Revesion\\Python_Logging_Example\\importance_of_inspect_module_part1.py', lineno=3, function='get_info', code_context=['    print(inspect.stack())#calling the Stack function in order to get the stack trace from where the request came in\n'], index=0), FrameInfo(frame=<frame at 0x00F0AA70, file 'C:/Users/611903295/Downloads/python/Django_Python_Revesion/Python_Logging_Example/importance_of_inspect_module_part2.py', line 4, code m1>, filename='C:/Users/611903295/Downloads/python/Django_Python_Revesion/Python_Logging_Example/importance_of_inspect_module_part2.py', lineno=4, function='m1', code_context=['    importance_of_inspect_module_part1.get_info()\n'], index=0), FrameInfo(frame=<frame at 0x00EB5C28, file 'C:/Users/611903295/Downloads/python/Django_Python_Revesion/Python_Logging_Example/importance_of_inspect_module_part2.py', line 5, code <module>>, filename='C:/Users/611903295/Downloads/python/Django_Python_Revesion/Python_Logging_Example/importance_of_inspect_module_part2.py', lineno=5, function='<module>', code_context=['m1()\n'], index=0)]


# FrameInfo(frame=<frame at 0x00BEAA70, file 'C:/Users/611903295/Downloads/python/Django_Python_Revesion/Python_Logging_Example/importance_of_inspect_module_part2.py', line 4, code m1>, filename='C:/Users/611903295/Downloads/python/Django_Python_Revesion/Python_Logging_Example/importance_of_inspect_module_part2.py', lineno=4, function='m1', code_context=['    importance_of_inspect_module_part1.get_info()\n'], index=0)

#m1
#C:/Users/611903295/Downloads/python/Django_Python_Revesion/Python_Logging_Example/importance_of_inspect_module_part2.py
