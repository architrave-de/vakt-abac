from flask import Flask, escape, request, jsonify
from policy import auth
import sys
from resources import USERS, DOCUMENTS

app = Flask(__name__)

@app.route('/api/users/', methods=['GET', 'POST'])
def users():
    api = request.path
    auth(request, api) # authenticate user to api
    return jsonify(USERS)


@app.route('/api/documents/', methods=['GET', 'POST'])
def documents():
    api = request.path
    auth(request, api)
    return jsonify(DOCUMENTS)

@app.route('/api/documents/<int:id>', methods=['GET', 'PUT'])
def document(id):
    document = None
    for d in DOCUMENTS:
        if d['id'] == id:
            document = d
            break 
    auth(request, document)
    return jsonify(document)

@app.route('/api/users/<int:id>', methods=['GET', 'PUT'])
def user(id):
    user = None
    for u in USERS:
        if u['id'] == id:
            user = u
            break 
    auth(request, user)
    return jsonify(user)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)