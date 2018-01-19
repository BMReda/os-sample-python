from flask import Flask,jsonify

from models import db, Application

application = Flask(__name__)

@application.route("/")
def hello():
    return "OpenShift Hello Le monde!"



@application.route("/applications")
def applications():
    #appli_name = Application.query.filter_by(name='appli_A').first()
    return "{ \"application\": [ { \"name\": \"appli_A\", \"qsi\": \"DPRS\" }, { \"name\": \"appli_B\", \"qsi\": \"DAL\" } ] }"


if __name__ == "__main__":
    application.run()

