from flask import Flask
from flask_restful import  Api 

from db import db
from resources.tramite import Tramite
from resources.establecimiento import Establecimiento
from resources.grado_riesgo import Riesgo

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secret_key_project'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

#endpoints
api.add_resource(Tramite, '/tramites')
api.add_resource(Establecimiento, '/establecimientos')
api.add_resource(Riesgo, '/autoevaluacion')


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)