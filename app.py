from flask import Flask, request, jsonify, send_from_directory
import os, uuid, subprocess, shutil
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

STATIC_DIR = os.path.join(os.getcwd(), "static")
RUNS_DIR = os.path.join(os.getcwd(), "runs")

os.makedirs(STATIC_DIR, exist_ok=True)
os.makedirs(RUNS_DIR, exist_ok=True)

@app.route("/execute", methods=["POST"])
def execute_script():
    data = request.json
    language = data.get("language")
    code = data.get("code")

    if language not in ["python", "r"]:
        return jsonify({"error": "Invalid language"}), 400

    session_id = str(uuid.uuid4())
    session_path = os.path.join(RUNS_DIR, session_id)
    os.makedirs(session_path, exist_ok=True)

    script_ext = "py" if language == "python" else "R"
    script_path = os.path.join(session_path, f"script.{script_ext}")

    with open(script_path, "w") as f:
        f.write(code)

    try:
        if language == "python":
            result = subprocess.run(
                ["python3", script_path],
                cwd=session_path,
                capture_output=True,
                timeout=20
            )
        else:
            result = subprocess.run(
                ["Rscript", script_path],
                cwd=session_path,
                capture_output=True,
                timeout=20
            )
    except subprocess.TimeoutExpired:
        return jsonify({"error": "Script execution timed out"}), 408

    if result.returncode != 0:
        return jsonify({"error": result.stderr.decode()}), 500

    for file in os.listdir(session_path):
        if file.endswith((".png", ".html")):
            file_path = os.path.join(session_path, file)
            shutil.copy(file_path, os.path.join(STATIC_DIR, f"{session_id}_{file}"))

            return jsonify({
                "url": f"http://127.0.0.1:5000/static/{session_id}_{file}"
            })

    return jsonify({"error": "No visualization generated"}), 500

@app.route("/static/<path:filename>")
def serve_static(filename):
    return send_from_directory(STATIC_DIR, filename)

if __name__ == "__main__":
    app.run(debug=True)