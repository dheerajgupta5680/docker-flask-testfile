import threading
from flask import Flask, jsonify, request
from services import supertel_testing, appscart_testing

app = Flask(__name__)


def run_task(task_func):
    # Utility function to run task in a new thread
    thread = threading.Thread(target=task_func)
    thread.start()
    
@app.route('/supertel', methods=['GET'])
def task1():
    username = request.args.get('username')
    password = request.args.get('password')
    
    # Validate username and password
    if username == 'admin' and password == 'asdf@1234':
        run_task(supertel_testing)
        return jsonify({"message": "supertel test run is in progress. You will be notified upon completion."})
    else:
        return jsonify({"message": "Invalid credentials"}), 401

@app.route('/appscart', methods=['GET'])
def tesk2():
    username = request.args.get('username')
    password = request.args.get('password')
    
    # Validate username and password
    if username == 'admin' and password == 'asdf@1234':
        run_task(appscart_testing)
        return jsonify({"message": "appscart test run is in progress. You will be notified upon completion."})
    else:
        return jsonify({"message": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)