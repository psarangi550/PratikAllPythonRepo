import pymysql #importing the pymsql module
con=pymysql.connect(host="localhost",port=3306,database="revesion",user="root",password="root")
cursor=con.cursor()#creating the cursor object
query="INSERT INTO employee (empid,empname,esal,eaddr) values (%s,%s,%s,%s)"
record=[(201,"Abismruta",20000,"Bangalore"),(301,"Priya",15000,"UK"),((401,"Priya",15000,"Hyderabad"))]
cursor.executemany(query,record)
print("Database Connected Successfully")
con.commit()
cursor.close()
con.close()