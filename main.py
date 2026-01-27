from query_router import get_score

while True:
    try:
        sbd = int(input("Nhập số báo danh (nhấn 0 để thoát): "))

        if sbd == 0:
            break

        result = get_score(sbd)

        if isinstance(result, str):
            print(result)
            continue
        else:
            print("\n=== KẾT QUẢ ===")
            print("Họ và tên:", result[0])
            print("Toán:", result[1])
            print("Văn:", result[2])
            print("Anh:", result[3])
            print("Lý:", result[4])
            print("Hóa:", result[5])
            print("Sinh:", result[6])

    except Exception as e:
        print(f"❌ Lỗi kết nối: {e}")

