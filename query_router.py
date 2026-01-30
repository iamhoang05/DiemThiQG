import pyodbc
from connect import NODE_BAC, NODE_TRUNG, NODE_NAM, DRIVER


def get_connection(node):
    conn_str = (
        f"DRIVER={{{DRIVER}}};"
        f"SERVER={node['server']};"
        f"DATABASE={node['database']};"
        f"UID=sa;"
        f"PWD=Matkhau@123;"
        "TrustServerCertificate=yes;"
        "Encrypt=no;"
    )

    return pyodbc.connect(conn_str, timeout=3)

def route_node(sbd):
    if 1 <= sbd <= 300:
        return NODE_BAC
    elif 301 <= sbd <= 600:
        return NODE_TRUNG
    elif 601 <= sbd <= 1000:
        return NODE_NAM
    else:
        return None


def get_score(sbd, node_status=None):
    node = route_node(sbd)
    if not node:
        return "SBD không hợp lệ!"

    # Kiểm tra xem node có đang "bật" không (giả lập)
    if node_status:
        if 1 <= sbd <= 300:
            node_id = "NODE_BAC"
        elif 301 <= sbd <= 600:
            node_id = "NODE_TRUNG"
        else:
            node_id = "NODE_NAM"
            
        if not node_status.get(node_id, True):
            return "Khu vực này đang bảo trì (Server Offline)"

    try:
        # Thử kết nối với timeout ngắn để phát hiện node offline nhanh
        #conn = get_connection(node) 
        conn = pyodbc.connect(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={node['server']};"
            f"DATABASE={node['database']};"
            f"UID={node['user']};"
            f"PWD={node['password']};"
            "TrustServerCertificate=yes;"
            "Encrypt=no;",
            timeout=3)
        cursor = conn.cursor()
        
        query = "SELECT HoTen, KhuVuc, DiemToan, DiemVan, DiemAnh, DiemLy, DiemHoa, DiemSinh FROM ThiSinh WHERE SBD = ?"
        cursor.execute(query, sbd)
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return row, node['database'] # Trả về dữ liệu và tên node xử lý
        else:
            return f"Không tìm thấy thí sinh với SBD {sbd} trong cơ sở dữ liệu."
        
    except Exception as e:
        # Trả về thông báo bảo trì
        print(f"Lỗi kết nối tới {node['database']}: {e}")
        return "Khu vực này đang bảo trì hoặc mất kết nối database"