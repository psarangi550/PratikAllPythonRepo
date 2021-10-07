try:
    print("statement code-1")
    print("statement code-2")
    print(10/0)
    print("statement code-3")
except ZeroDivisionError as e:
    print(10/0)
    print("ZeroDivision Error ")