from flask import Flask, request
from flask import jsonify
import json

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

@app.route('/get_text_suggestions', methods=['POST'])
def get_text_suggestions_():
    try:
        res = {'suggestions': ['This','is','Test']}
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
