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
            print("Khu vực: ", result[1])
            print("Toán:", result[2])
            print("Văn:", result[3])
            print("Anh:", result[4])
            print("Lý:", result[5])
            print("Hóa:", result[6])
            print("Sinh:", result[7])

    except Exception as e:
        print(f"❌ Lỗi kết nối: {e}")

