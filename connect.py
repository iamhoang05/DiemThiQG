import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost,1433;"
    "DATABASE=master;"
    "UID=sa;"
    "PWD=Hoangnguyen712@;"
    "TrustServerCertificate=yes;"
)

NODE_BAC = {
    "server": "localhost,1433",
    "database": "THISINH_BAC",
    "user": "sa",
    "password": "Hoangnguyen712@"
}

NODE_NAM = {
    "server": "localhost,1433",
    "database": "THISINH_NAM",
    "user": "sa",
    "password": "Hoangnguyen712@"
}

DRIVER = "ODBC Driver 17 for SQL Server"
print("✅ CONNECT OK")
conn.close()
