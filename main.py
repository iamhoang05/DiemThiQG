from flask import Flask, render_template, request, jsonify
from query_router import get_score, NODE_STATUS

app = Flask(__name__)

# --- ROUTE 1: TRANG CHỦ ---
@app.route('/', methods=['GET', 'POST'])
def index():
    result_data = None
    error_msg = None
    sbd_input = ""
    user_region = request.form.get('user_region', 'BAC') # Lấy vị trí đã chọn

    if request.method == 'POST':
        sbd_input = request.form.get('sbd')
        try:
            result = get_score(int(sbd_input), user_region)
            if isinstance(result, str):
                error_msg = result
            else:
                result_data = result
        except ValueError:
            error_msg = "Vui lòng nhập số báo danh là chữ số!"

    # QUAN TRỌNG
    return render_template('index.html', 
                           data=result_data, 
                           error=error_msg, 
                           sbd=sbd_input, 
                           node_status=NODE_STATUS, 
                           user_region=user_region)

# --- ROUTE 2: ĐIỀU KHIỂN BẬT/TẮT (PHẢI NẰM TRÊN APP.RUN) ---
@app.route('/manage_db', methods=['POST'])
def manage_db():
    data = request.json
    region = data.get('region') # 'BAC' hoặc 'NAM'
    action = data.get('action') # 'on' hoặc 'off'
    
    # Cập nhật trạng thái giả lập
    NODE_STATUS[region] = (action == 'on')
    msg = f"Miền {region} đã {'BẬT' if action == 'on' else 'TẮT'}"
    return jsonify({"status": "success", "message": msg})

# --- CHẠY SERVER ---
if __name__ == '__main__':
    app.run(debug=True)