import pymysql #importing the pymsql module
con=pymysql.connect(host="localhost",port=3306,database="revesion",user="root",password="root")
cursor=con.cursor()#creating the cursor object
cursor.execute("INSERT INTO employee values (101,'Pratik',1000.00,'Bangalore')")
print("Database Connected Successfully")
con.commit()
cursor.close()
con.close()