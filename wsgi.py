from flask import Flask
application = Flask(__name__)

@application.route("/hello", methods=['GET'])
def hello():
    operator = request.args.get('operator')
    return operator

if __name__ == "__main__":
    application.run()
