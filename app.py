"""CHỐT VIỆC – chạy website cục bộ bằng Flask.

Cách chạy trong PyCharm:
  1. Mở thư mục chot_viec bằng PyCharm (File > Open).
  2. Tạo/chọn interpreter (venv), PyCharm sẽ gợi ý cài requirements.txt.
  3. Chuột phải app.py > Run 'app'.
  4. Mở http://127.0.0.1:5000
"""
import threading
import webbrowser
from pathlib import Path

from flask import Flask, send_from_directory

BASE_DIR = Path(__file__).resolve().parent
SITE_DIR = BASE_DIR / "site"

app = Flask(__name__, static_folder=None)


@app.route("/")
def index():
    return send_from_directory(SITE_DIR, "index.html")


@app.route("/<path:filename>")
def assets(filename):
    # Phục vụ thêm file tĩnh (ảnh, css, js...) nếu bạn đặt vào thư mục site/
    return send_from_directory(SITE_DIR, filename)


if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 5000
    # Tự mở trình duyệt sau 1 giây (tránh mở 2 lần khi bật debug reloader)
    threading.Timer(1.0, lambda: webbrowser.open(f"http://{HOST}:{PORT}")).start()
    app.run(host=HOST, port=PORT, debug=False)
