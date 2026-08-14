from flask import Flask, jsonify, request, send_file

app = Flask(__name__)
scenarios = []

@app.route("/")
def home():
    return "Server Running"

@app.route("/api/scenarios", methods=["GET", "POST"])
def scenarios_api():
    if request.method == "POST":
        data = request.get_json()
        scenarios.append(data)
        return jsonify({"status": "success", "total": len(scenarios)})
    return jsonify(scenarios)

@app.route("/api/stats")
def stats():
    return jsonify({"total_scenarios": len(scenarios)})

@app.route("/backup")
def backup():
    f = open("backup.txt", "w")
    f.write("backup ok")
    f.close()
    return send_file("backup.txt", as_attachment=True)

if __name__ == "__main__":
    app.run()
    #PR to sir
