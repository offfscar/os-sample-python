from flask import Flask, request
application = Flask(__name__)

@application.route("/hello", methods=['GET'])
def hello():
    operator = request.args.get('operator')
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    return num1 + num2

if __name__ == "__main__":
    application.run()
