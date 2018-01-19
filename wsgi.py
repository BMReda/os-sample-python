from flask import Flask,jsonify

from models import db, Application

from sqlalchemy_jsonapi import JSONAPI


application = Flask(__name__)

# define your models classes hereafter
POSTGRES = {
    'user': 'myappuser',
    'pw': 'azerty1234',
    'db': 'sampledb',
    'host': '172.30.145.206',
    'port': '5432',
}
application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db.init_app(application)

@application.route("/")
def hello():
    return "OpenShift Hello Le monde!"



@application.route("/applications")
def applications():
    #appli_name = Application.query.filter_by(name='appli_A').first()
    #return appli_name.name + " - " + appli_name.qsi
    response = JSONAPI(Application).get_collection(db.session, {}, 'application')
    return jsonify(response.data)


if __name__ == "__main__":
    application.run()

