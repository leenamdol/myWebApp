from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, world!</p>"

@app.route("/fastcampus")
def hello_fastcampus():
    return "<p>Hello, Fast Campus!</p>"

@app.route("/predict", methods=["POST","PUT"])
def inference():
    return json.dumps({'hello': 'world'}), 200  # http status code

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
    