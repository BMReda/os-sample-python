from flask import Flask
application = Flask(__name__)


@application.route("/")
def hello():
    return "OpenShift Hello Le monde!"


@application.route("/applications")
def applications():
    return "application A"


if __name__ == "__main__":
    application.run()
