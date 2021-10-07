import psycopg2 #importing the psycopg2 for connecting to postgres DB
DB_NAME="rniwkgcm"
DB_PORT="5432"
DB_HOST="chunee.db.elephantsql.com"
DB_USER="rniwkgcm"
DB_PASS="TRSRv_NHaXzhxIcx3feJRylxk6oJtnAt"
con=psycopg2.connect(database=DB_NAME,host=DB_HOST,port=DB_PORT,user=DB_USER,password=DB_PASS)
cursor=con.cursor()
values=(401,'Priya',85000,'UK')
cursor.execute("""INSERT INTO public."Employee"(
	empid, empname, esal, eaddr)
	VALUES (%s, %s, %s, %s);""", values)
con.commit()
cursor.close()
con.close()