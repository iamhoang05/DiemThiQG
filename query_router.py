import pyodbc
from connect import NODE_BAC, NODE_NAM, DRIVER

# Biến toàn cục để giả lập trạng thái Node (Bật/Tắt từ giao diện)
NODE_STATUS = {
    "BAC": True,
    "NAM": True
}

def route_node(sbd):
    """Xác định node chứa dữ liệu dựa trên dải SBD"""
    if 1 <= sbd <= 500:
        return NODE_BAC
    elif 501 <= sbd <= 1000:
        return NODE_NAM
    return None

def get_score(sbd, user_region):
    # BƯỚC 1: XÁC ĐỊNH KHU VỰC CỦA SBD (Validation dải dữ liệu)
    if 1 <= sbd <= 500:
        target_region = "BAC"
    elif 501 <= sbd <= 1000:
        target_region = "NAM"
    else:
        return "Số báo danh không tồn tại trong hệ thống (1-1000)!"

    # BƯỚC 2: KIỂM TRA KHỚP VỊ TRÍ (Đúng yêu cầu của bạn)
    # Nếu bạn ở trạm Bắc mà tra cứu SBD Nam, báo lỗi không khớp vùng ngay lập tức
    if user_region != target_region:
        return f"Số báo danh {sbd} không thuộc quyền quản lý của trạm Miền {user_region}!"

    # BƯỚC 3: KIỂM TRA TRẠNG THÁI TRẠM TẠI CHỖ (Status Check)
    # Chỉ khi đã khớp vùng, chúng ta mới xét xem trạm đó có đang "Bảo trì" hay không
    if not NODE_STATUS.get(user_region, True):
        return f"Hệ thống tại trạm Miền {user_region} đang bảo trì, vui lòng quay lại sau!"

    # BƯỚC 4: TIẾN HÀNH TRUY VẤN VẬT LÝ
    node = route_node(sbd)
    try:
        conn = pyodbc.connect(
            f"DRIVER={{{DRIVER}}};"
            f"SERVER={node['server']};"
            f"DATABASE={node['database']};"
            f"UID={node['user']};"
            f"PWD={node['password']};"
            "TrustServerCertificate=yes;",
            timeout=3
        )
        cursor = conn.cursor()
        query = "SELECT HoTen, KhuVuc, DiemToan, DiemVan, DiemAnh, DiemLy, DiemHoa, DiemSinh FROM ThiSinh WHERE SBD = ?"
        cursor.execute(query, sbd)
        row = cursor.fetchone()
        conn.close()
        
        return row if row else "Không tìm thấy dữ liệu thí sinh."
        
    except Exception as e:
        print(f"Lỗi kết nối vật lý tới {node['database']}: {e}")
        return f"Máy chủ {user_region} đang mất kết nối vật lý (SQL Service Offline)."