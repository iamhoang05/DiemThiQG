import pyodbc
from connect import NODE_BAC, NODE_NAM, DRIVER


def get_connection(node):
    conn_str = (
        f"DRIVER={{{DRIVER}}};"
        f"SERVER={node['server']};"
        f"DATABASE={node['database']};"
        f"UID=sa;"
        f"PWD=Hoangnguyen712@;"
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
        print(f"🔍 Đang kết nối tới {node['database']} ...")

        conn = get_connection(node)

        print(f"✅ Kết nối {node['database']} thành công!")

        cursor = conn.cursor()

        query = """
            SELECT HoTen, KhuVuc, DiemToan, DiemVan, DiemAnh, DiemLy, DiemHoa, DiemSinh 
            FROM ThiSinh 
            WHERE SBD = ?
        """
        
        cursor.execute(query, sbd)
        row = cursor.fetchone()
        conn.close()

        if row:
            return row  
        else:
            return "⚠️ Không tìm thấy thí sinh này trong dữ liệu."

    except Exception as e:
        print(f"❌ Lỗi khi kết nối {node['database']}: {repr(e)}")



