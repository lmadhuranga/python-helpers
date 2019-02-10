import os
from flask import Flask, flash, request, jsonify

auth=['authentic1']

app = Flask(__name__)

def checkAuth():
    error = None
    # Check method type is post 
    if request.method=='POST':
        # Check Authenications
        try:
            token = request.headers['API_TOKEN']
            # Check auth token is valied
            if token not in auth:
                error = {'error':'Unauthorized', 'satus_code':401}
        except Exception as e:
            error = {'error':'Unauthorized', 'satus_code':401}
    else:
        error = {'error':'Not found', 'satus_code':404}
    return error

@app.route('/hello',methods=['POST', 'GET'])
def hello():
    # Check the autentication status
    authStatus = checkAuth()
    if authStatus != None :
        return jsonify(authStatus), authStatus['satus_code']
    else:
        return jsonify({'msg':'ok to work 200'})
        
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)