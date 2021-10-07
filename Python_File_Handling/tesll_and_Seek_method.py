with open("demo.txt") as f:
    f.seek(0)
    print(f.read(10))
    print(f.tell())