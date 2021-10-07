try:
    print("statement-1")
    print("statement-2")
    print("statement-3")
    try:
        print("statement-4")
        # print("Statement-5")
        print(10/0)
        print("Statement:-6")
    except:
        # print("Statement-7")
        print(10/0)
    finally:
        print("Statement-8")
    print("Statement-9")
except:
    print("Statement:-10")
finally:
    print("Statement-11")
print("Statement-12")