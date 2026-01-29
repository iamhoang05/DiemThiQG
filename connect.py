import os
import pyodbc
from dotenv import load_dotenv
load_dotenv()
#lay thong tin
SERVER = os.getenv('DB_SERVER')
UID = os.getenv('DB_USER')
PWD = os.getenv('DB_PASSWORD')
conn_str = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={SERVER};"
    "DATABASE=master;"
    f"UID={UID};"
    f"PWD={PWD};"
    "TrustServerCertificate=yes;"
)
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost,1433;"
    "DATABASE=master;"
    "UID=sa;"
    "PWD=Matkhau;"
    "TrustServerCertificate=yes;"
)

NODE_BAC = {
    "server": "localhost,1433",
    "database": "THISINH_BAC",
    "user": "sa",
    "password": "Matkhau"
}

NODE_NAM = {
    "server": "localhost,1433",
    "database": "THISINH_NAM",
    "user": "sa",
    "password": "Matkhau"
}

DRIVER = "ODBC Driver 17 for SQL Server"
print("CONNECT OK")
conn.close()
