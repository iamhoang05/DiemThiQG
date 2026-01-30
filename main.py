from flask import Flask, render_template, request
from query_router import get_score

app = Flask(__name__)

# Quản lý trạng thái các node (giả lập bật/tắt)
node_status = {
    "NODE_BAC": True,
    "NODE_TRUNG": True,
    "NODE_NAM": True
}

@app.route('/', methods=['GET', 'POST'])
def index():
    result_data = None
    error_msg = None
    sbd_input = ""

    if request.method == 'POST':
        sbd_input = request.form.get('sbd')
        try:
            # Logic này sẽ được tích hợp vào query_router, nhưng ta truyền status vào
            result = get_score(int(sbd_input), node_status)

            if isinstance(result, str):
                error_msg = result
            else:
                result_data, processed_node = result # Giải nén tuple (data, node_name)
        except ValueError:
            error_msg = "Vui lòng nhập số báo danh là chữ số!"
        except Exception as e:
            error_msg = f"Lỗi hệ thống: {e}"

    return render_template('index.html', 
                           data=result_data, 
                           processed_node=processed_node if 'processed_node' in locals() else None,
                           error=error_msg, 
                           sbd=sbd_input,
                           node_status=node_status)

@app.route('/toggle/<node_name>')
def toggle_node(node_name):
    if node_name in node_status:
        node_status[node_name] = not node_status[node_name]
    return "OK"

if __name__ == '__main__':
    app.run(debug=True)