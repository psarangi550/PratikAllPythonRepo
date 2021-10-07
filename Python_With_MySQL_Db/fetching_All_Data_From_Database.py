import pymysql #importing the pymysql module
con=pymysql.connect(host="localhost",port=3306,database="revesion",user="root",password="root")
cursor=con.cursor()
cursor.execute("SELECT * FROM employee")
# datas=cursor.fetchall()
datas=cursor.fetchmany(3)
for data in datas:
    print(f"Employee id is {data[0]}")
    print(f"Employee Name is {data[1]}")
    print(f"Employee Salary is {data[2]}")
    print(f"Employee Address is {data[3]}")
    print()
cursor.close()
con.close()
