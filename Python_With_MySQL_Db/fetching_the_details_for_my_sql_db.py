import pymysql #importing the pymysql module
con=pymysql.connect(host="localhost",port=3306,database="revesion",user="root",password="root")
cursor=con.cursor()
cursor.execute("SELECT * FROM employee")
data=cursor.fetchone()
while True:
    if data is not None:
        print(data)
        data = cursor.fetchone()
cursor.close()
con.close()
