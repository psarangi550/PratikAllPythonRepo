import psycopg2 #importing the psycopg2 for connecting to postgres DB
DB_NAME="rniwkgcm"
DB_PORT="5432"
DB_HOST="chunee.db.elephantsql.com"
DB_USER="rniwkgcm"
DB_PASS="TRSRv_NHaXzhxIcx3feJRylxk6oJtnAt"
con=psycopg2.connect(database=DB_NAME,host=DB_HOST,port=DB_PORT,user=DB_USER,password=DB_PASS)
cursor=con.cursor()
#here we want to select all the items from the postgre elephant SQL DB
cursor.execute("""SELECT * FROM public."Employee" """)
# print(cursor.fetchone())
print(cursor.fetchall())