from flask import Flask, jsonify
import sys
app=Flask(__name__)
@app.route('/api/hello')
def hello():
    response={'message': 'Hello, this is your Flask API!'}
    return jsonify(response)
if __name__ == '__main__':
    port=int(sys.argv[1] if len(sys.argv)>1 else 5000)
    app.run(host='0.0.0.0',port=port)