from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Pariwar API running"}

@app.route("/patients", methods=["POST"])
def add_patient():
    data = request.json
    if not data.get("name"):
        return {"error": "Name required"}, 400
    return {"message": "Patient added", "data": data}

if __name__ == "__main__":
    app.run(debug=True)
