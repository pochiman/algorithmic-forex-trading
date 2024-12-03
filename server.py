from flask import Flask, jsonify
from flask_cors import CORS

from scraping.bloomberg_com import bloomberg_com

app = Flask(__name__)
CORS(app)

@app.route("/api/test")
def test():
    return jsonify(dict(message='hello'))

@app.route("/api/headlines")
def headlines():
    return jsonify(bloomberg_com())


if __name__ == "__main__":
    app.run(debug=True)
