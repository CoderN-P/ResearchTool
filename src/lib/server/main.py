from flask import Flask, request, jsonify, make_response
from dotenv import load_dotenv
from summarize_articles import summarize_articles

load_dotenv()

app = Flask(__name__)

FRONTEND_URL = "http://localhost:5173"


@app.route('/fetch-summary', methods=['POST', 'OPTIONS'])
def fetch_summary():
    if request.method == "OPTIONS":  # CORS preflight
        return _build_cors_preflight_response()
    elif request.method == "POST":  # The actual request following the preflight
        prompt = request.json['prompt']

        data = summarize_articles(prompt)

        return _corsify_actual_response(jsonify(data))
    else:
        raise RuntimeError("Weird - don't know how to handle method {}".format(request.method))


def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response


def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == '__main__':
    app.run(port=5000)
