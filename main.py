# -*- coding: utf-8 -*-

from flask import request, make_response, jsonify
import random
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world(methods = ['POST', 'GET']):
    # print(type(request.args.get("txt")))
    # print(request.args.get("txt").encode('utf-8'))
    # if 'დაბადების დღე' in request.args.get("txt").encode('utf-8'):
    #     return jsonify({"stat":[1,2,1,1]})
    # else:
    return jsonify({"stat":[random.randint(0, 5),random.randint(0, 5),random.randint(0, 5),random.randint(0, 5), random.randint(0, 5)]})
    # return jsonify({"stat":[1,2,7,3]})

if __name__ == "__main__":
    app.run(ssl_context=('cert.pem', 'key.pem'))


@app.after_request
def after_request_func(response):
    origin = request.headers.get('Origin')
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Headers', 'x-csrf-token')
        response.headers.add('Access-Control-Allow-Methods',
                            'GET, POST, OPTIONS, PUT, PATCH, DELETE')
        if origin:
            response.headers.add('Access-Control-Allow-Origin', origin)
    else:
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        if origin:
            response.headers.add('Access-Control-Allow-Origin', origin)

    return response 