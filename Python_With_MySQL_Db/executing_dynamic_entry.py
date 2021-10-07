import pymysql #importing the pymsql module
con=pymysql.connect(host="localhost",port=3306,database="revesion",user="root",password="root")
cursor=con.cursor()#creating the cursor object
while True:
    empid=int(input("Enter Employee Id"))
    empname=input("Enter Employee Name")
    esal=float(input("Enter Employee Salary"))
    eaddr=input("Enter Employee Address")
    query=f"INSERT INTO employee values ({empid},'{empname}',{esal},'{eaddr}')"
    cursor.execute(query)
    option=input("Do you wish to Add One More record [y]/[n] only")
    if option.lower()=="n":
        con.commit()
        break
cursor.close()
con.close()
