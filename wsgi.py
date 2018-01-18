from flask import Flask
application = Flask(__name__)


@application.route("/test")
def hello():
    return "OpenShift Hello World!"


@application.route("/applications")
def applications():
    return "application A"


if __name__ == "__main__":
    application.run()
