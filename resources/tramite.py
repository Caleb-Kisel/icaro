from flask_restful import Resource, reqparse
from models.tramite import TramiteModel

class Tramite(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('usuario_fk',
                        type=int,
                        required=True,
                        help="Cada tramite radica en un usuario."
                        )

    def get(self):
        data = Tramite.parser.parse_args()
        tramite = TramiteModel.find_by_user(data['usuario_fk'])
        if tramite:
            return {'tramites': [x.json() for x in tramite]}
        return {'Error': 'No hay tramites para dicho usuario.'}, 404

#return {'tramites': [x.json() for x in TramiteModel.find_by_user(user)]}