from flask import Flask, request
from flask import jsonify
import json
from pipelines.main import LangModelPipeline
import google.cloud.logging
import logging

# Setup logging
client = google.cloud.logging.Client()
client.get_default_handler()
client.setup_logging()

# Setup text suggestion pipeline
pipe_params = {
        'model_name': 'bert-base-uncased',
        'topK_for_completions': 10000,
        'topK_for_biasing': 10,
        'split_sents': True,
        'contraction_action': True
}
pipeline = LangModelPipeline(**pipe_params)

# Setup text suggestion service
app = Flask(__name__)

# Needed to add CORS support
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    if request.method == 'OPTIONS':
        response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, POST, PUT'
        headers = request.headers.get('Access-Control-Request-Headers')
        if headers:
            response.headers['Access-Control-Allow-Headers'] = headers
    return response
app.after_request(add_cors_headers)

@app.route('/')
def hello():
    dictionary = {'message': 'Hello from North AIMC!'}
    return jsonify(dictionary)

@app.route('/post_log', methods=['POST'])
def post_log_():
    try:
        # Log event data
        logging.info(json.dumps(request.json))
        res = {'message':'event data logged'}
        return app.response_class(response=json.dumps(res),
            status=200, mimetype='application/json')
    except Exception as error:
        err = str(error)
        return app.response_class(response=json.dumps(err),
            status=500, mimetype='application/json')

@app.route('/get_text_suggestions', methods=['POST'])
def get_text_suggestions_():
    try:
        text = request.json['input_text']
        group = request.json['sentiment_bias']
        res = {'suggestions':pipeline.get_suggestions(text,group)}
        # Log request data and response data
        return app.response_class(response=json.dumps(res),
            status=200, mimetype='application/json')
    except Exception as error:
        err = str(error)
        return app.response_class(response=json.dumps(err),
            status=500, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=8080, debug=True, use_reloader=False)

#curl -X POST "https://python-dot-north-aimc.nw.r.appspot.com/get_text_suggestions" -H "Content-Type: application/json" -d "{\"input_text\":\"This is \",\"sentiment_bias\":\"1\"}"
#curl -X POST "http://0.0.0.0:8080/get_text_suggestions" -H "Content-Type: application/json" -d "{\"input_text\":\"This is \",\"sentiment_bias\":\"1\"}"
#curl -X POST "http://127.0.0.1:5000/get_text_suggestions" -H "Content-Type: application/json" -d "{\"input_text\":\"This is \",\"sentiment_bias\":\"1\"}"
