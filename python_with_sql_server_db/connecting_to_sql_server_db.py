import pyodbc #importing the pyodbc module in order to connect the python to sql server db
try:
    con=pyodbc.connect(
                    Driver="{SQL Server Native Client 11.0};",
                    server="BANTM340003600",
                    Database="PratikDatabase",
                    Trusted_Connection="Yes"
                    )
except:
    print("connection_unsuccessfull")