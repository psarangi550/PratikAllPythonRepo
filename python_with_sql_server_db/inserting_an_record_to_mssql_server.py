import pyodbc
con=pyodbc.connect(
    Driver="{SQL Server Native Client 11.0};",
    Server="BANTM340003600",
    Database="PratikDatabase",
    Trusted_Connection="yes"
)
cursor=con.cursor()
cursor.execute("""SELECT * from dbo.employee""")
print(cursor.fetchone())
print(cursor.fetchmany())
print(cursor.fetchall())
cursor.close()
con.close()