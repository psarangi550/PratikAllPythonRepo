import sqlite3 #importing the sqlite3 database
import Employee_Demo_module
con=sqlite3.connect("Employee1.db")
cursor=con.cursor()

# emp_1=Employee_Demo_module.Employee("Abismruta","Sarangi",50000)
# emp_2=Employee_Demo_module.Employee("prateekshya","Sarangi",40000)
emp_4=Employee_Demo_module.Employee("pratik","Sarangi",20000)

# # creating the Table
# ---------------------
# cursor.execute("""CREATE TABLE Employee1 (
#                     first text,
#                     second text,
#                     pay integer
#                     )""")
# con.commit()

def insert_employee(emp):
    with con:
        cursor.execute("INSERT INTO Employee1 (first, second, pay) VALUES (:first,:second,:pay)",
                       {"first":emp.first,"second":emp.second,"pay":emp.pay})
def get_employee(emp):
    cursor.execute("SELECT * From Employee1 WHERE first=:first", {"first":emp.first})
    print(cursor.fetchone())
def update_employee(emp,pay):
    with con:
        cursor.execute(f"UPDATE Employee1 SET pay={pay} WHERE first=:first",{"first":emp.first})
    get_employee(emp)
def remove_employee(emp):
    with con:
        cursor.execute("DELETE FROm Employee1 WHERE first=:first",{"first":emp.first})


# insert_employee(emp_4)
# get_employee(emp_4)
# update_employee(emp_4,10000)
remove_employee(emp_4)

#insertingonly one record:-
#---------------------------
# cursor.execute("INSERT INTO Employee (first,second,pay) VALUES ('Pratik','Sarangi',10000)")
# con.commit()
# print("Data Inserted")

#creating the employee object in here
# emp_1=Employee_Demo_module.Employee("Abismruta","Sarangi",50000)
# emp_2=Employee_Demo_module.Employee("prateekshya","Sarangi",40000)

# #inserting Multiple column at a time:-1st approach
# cursor.execute("INSERT INTO Employee(first,second,pay) VALUES (?,?,?)", (emp_1.first,emp_1.second,emp_1.pay))
# con.commit()

# #inserting Multiple column at a time:-2nd approach
# cursor.execute("INSERT INTO Employee(first,second,pay) VALUES (:first,:second,:pay)", {"first":emp_2.first,"second":emp_2.second,"pay":emp_2.pay})
# con.commit()


#select with where clause and parameterized value as:-1st approach
# cursor.execute("SELECT * From Employee WHERE first=?", (emp_1.first,))


#second_Approach:-
# cursor.execute("SELECT * From Employee WHERE first=:first", {"first":emp_1.first,})

# cursor.execute("select * from Employee")

# print(cursor.fetchone())
# print(cursor.fetchall())
# print(cursor.fetchmany(2))

cursor.close()
con.close()