import pymysql #imprting pymysql module
con=pymysql.connect(host="localhost",port=3306,database="revesion",user="root",password="root")
if con is not None:
    print("Successfull connection")
    print(con.server_version)
    con.close()
else:
    print("Connection Unsuccessful")

