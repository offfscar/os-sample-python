from flask import Flask, request
application = Flask(__name__)

@application.route("/hello", methods=['GET'])
def hello():
    operator = request.args.get('operator')
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))

    if operator == 'add':
        result = num1 + num2
    elif operator == 'sub':
        result = num1 - num2
    elif operator == 'mul':
        result = num1 * num2
    elif operator == 'div':
        result = num1 / num2
    return 'El reultado es ' + str(result)

if __name__ == "__main__":
    application.run()
