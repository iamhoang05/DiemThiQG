from flask import Flask, render_template, request
from query_router import get_score

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result_data = None
    error_msg = None
    sbd_input = ""

    if request.method == 'POST':
        sbd_input = request.form.get('sbd')
        try:
            # Chuyển sbd sang int và gọi hàm từ query_router.py
            result = get_score(int(sbd_input))

            if isinstance(result, str):
                error_msg = result
            else:
                result_data = result
        except ValueError:
            error_msg = "Vui lòng nhập số báo danh là chữ số!"
        except Exception as e:
            error_msg = f"Lỗi hệ thống: {e}"

    return render_template('index.html', data=result_data, error=error_msg, sbd=sbd_input)

if __name__ == '__main__':
    app.run(debug=True)