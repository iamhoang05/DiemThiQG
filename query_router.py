import pyodbc
from connect import NODE_BAC, NODE_NAM, DRIVER


def get_connection(node):
    conn_str = (
        f"DRIVER={{{DRIVER}}};"
        f"SERVER={node['server']};"
        f"DATABASE={node['database']};"
        f"UID=sa;"
        f"PWD=Matkhau;"
        f"TrustServerCertificate=yes;"
    )

    return pyodbc.connect(conn_str, timeout=3)

def route_node(sbd):
    if 1 <= sbd <= 500:
        return NODE_BAC
    elif 501 <= sbd <= 1000:
        return NODE_NAM
    else:
        return None


def get_score(sbd):
    node = route_node(sbd)
    if not node:
        return "SBD không hợp lệ!"

    try:
        # Thử kết nối với timeout ngắn để phát hiện node offline nhanh
        #conn = get_connection(node) 
        conn = pyodbc.connect(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={node['server']};"
            f"DATABASE={node['database']};"
            f"UID={node['user']};"
            f"PWD={node['password']};"
            "TrustServerCertificate=yes;",
            timeout=3)
        cursor = conn.cursor()
        
        query = "SELECT HoTen, KhuVuc, DiemToan, DiemVan, DiemAnh, DiemLy, DiemHoa, DiemSinh FROM ThiSinh WHERE SBD = ?"
        cursor.execute(query, sbd)
        row = cursor.fetchone()
        conn.close()
        
        return row # Trả về dữ liệu nếu thành công
        
    except Exception as e:
        # Trả về thông báo bảo trì
        print(f"Lỗi kết nối tới {node['database']}: {e}")
        return "Khu vực này đang bảo trì"