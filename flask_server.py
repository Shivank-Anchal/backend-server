from flask import Flask,jsonify,request
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

@app.route('/api/authenticate',methods=['POST'])
def post_request():
    if request.method == 'POST':
        print("=====>>> Post request")
        print(request.data)
        return jsonify({"response":"post request accepted"}) 

    else:
        return jsonify({"response":"post request not accepted"}) 

if __name__=='__main__':
    app.run(debug=True)