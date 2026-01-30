import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=127.0.0.1;"
    "DATABASE=master;"
    "UID=sa;"
    "PWD=Matkhau;"
    "TrustServerCertificate=yes;"
)

NODE_BAC = {
    "server": "127.0.0.1;",
    "database": "THISINH_BAC",
    "user": "sa",
    "password": "Matkhau"
}

NODE_NAM = {
    "server": "127.0.0.1;",
    "database": "THISINH_NAM",
    "user": "sa",
    "password": "Matkhau"
}

DRIVER = "ODBC Driver 17 for SQL Server"
print("CONNECT OK")
conn.close()
