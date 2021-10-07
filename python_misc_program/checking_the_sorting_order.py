class Employee(object):
    def __init__(self,ename,age,salary):
        self.ename=ename
        self.age=age
        self.salary=salary
    def __repr__(self):
        return f"[{self.ename},{self.age},{self.salary}]"
def employee_sorting(emp):
    return emp.salary
e1=Employee("pratik",30,10000)
e2=Employee("Rika",24,20000)
e3=Employee("Papali",26,30000)
list1=[e1,e2,e3]
list1.sort(key=employee_sorting,reverse=True)
print(list1)
list2=list(sorted(list1,key=employee_sorting))
print(list2)
