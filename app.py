import socket
import threading
import webbrowser
from flask import Flask, render_template, jsonify, send_from_directory
from file_system import create_databases, FileSystem

app = Flask(__name__)

# --- ROUTES ---
@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/image")
def image_page():
    return render_template("image.html")

@app.route("/video")
def video_page():
    return render_template("video.html")

@app.route("/music")
def music_page():
    return render_template("music.html")

@app.route("/document")
def document_page():
    return render_template("document.html")

@app.route("/executable")
def executable_page():
    return render_template("executable.html")

@app.route("/archive")
def archive_page():
    return render_template("archive.html")

# --- FUNCTIONALITY ---
FILE_PATH = FileSystem.DOWNLOADS
@app.route('/file/<path:filename>')
def download_file(filename):
    return send_from_directory(FILE_PATH, filename, as_attachment=True)

@app.route("/database/<filename>")
def database_file(filename):
    return send_from_directory("database", filename)

@app.route("/create_database", methods=["POST"])
def create_databases():
    try:
        create_databases()
        msg = "successfully!"
        return jsonify({"success": True, "message": msg}), 200
    except Exception as e:
        error_msg = str(e)
        return jsonify({"success": False, "error": error_msg}), 500

# --- UTILITIES ---
def get_local_ip() -> str:
    """Reliably determine the local LAN IP address."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            # Does not transmit actual packets; used to select active network interface
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except Exception:
        return "127.0.0.1"


# --- APPLICATION ENTRYPOINT ---
# if __name__ == "__main__":
#     PORT = 5009
#     local_ip = get_local_ip()
#     url = f"http://{local_ip}:{PORT}"

#     print(f" * Serving Flask app on {url}")

#     # Open browser slightly delayed in a background thread to allow server startup
#     threading.Timer(1.2, lambda: webbrowser.open(url)).start()

#     # Run server (host='0.0.0.0' allows both local machine and local LAN access)
#     app.run(host="0.0.0.0", port=PORT, debug=True)


# if __name__ == "__main__":
#     app.run(debug=True)

# Get local IP address
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

if __name__ == "__main__":
    port = 5009
    webbrowser.open(f"http://{local_ip}:{port}")
    app.run(host=local_ip, port=port)