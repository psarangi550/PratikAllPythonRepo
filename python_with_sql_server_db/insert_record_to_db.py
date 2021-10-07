import pyodbc
con=pyodbc.connect(
    Driver="{SQL Server Native Client 11.0};",
    Server="BANTM340003600",
    Database="PratikDatabase",
    Trusted_Connection="yes"
)
cursor=con.cursor()
cursor.execute("""INSERT INTO dbo.employee VALUES (901,'Rika',90000,'Bangalore')""")
con.commit()
cursor.close()
con.close()