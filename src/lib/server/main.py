from flask import Flask, request, jsonify
from dotenv import load_dotenv
from .summarize_articles import summarize_articles

load_dotenv()

app = Flask(__name__)


@app.route('/fetch-summary', method=['POST'])
def fetch_summary():
    prompt = request.json['prompt']

    data = summarize_articles(prompt)

    return jsonify(data)


if __name__ == '__main__':
    app.run(port=5000)



