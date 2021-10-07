import psycopg2 #importing the psycopg2 for connecting to postgres DB
DB_NAME="rniwkgcm"
DB_PORT="5432"
DB_HOST="chunee.db.elephantsql.com"
DB_USER="rniwkgcm"
DB_PASS="TRSRv_NHaXzhxIcx3feJRylxk6oJtnAt"
try:
    con=psycopg2.connect(database=DB_NAME,hostname=DB_HOST,port=DB_PORT,username=DB_USER,password=DB_PASS)
    con.close()
except:
    print("Connection Successful")
else:
    print("Connection Successful")