from flask_restful import Resource
from models.establecimiento import EstablecimientoModel
from flask import request


class Establecimiento(Resource):
    # request_data = request.get_json()
    
    def post(self):
        request_data = request.get_json()
        name = request_data['nombre']

        if EstablecimientoModel.find_by_name(name):
            return {'Error': "Un establecimiento con el nombre '{}' ya existe.".format(name)}, 400

        establecimiento = EstablecimientoModel(**request_data,)

        try:
            establecimiento.save_to_db()
        except:
            return {'Error': "Un error ocurrio insertando el establecimiento."}, 500

        return establecimiento.json(), 201

    def put(self):
        request_data = request.get_json()
        name = request_data['nombre']
        exist = EstablecimientoModel.find_by_name(name)

        if exist:
            exist.delete_from_db()

        establecimiento = EstablecimientoModel(**request_data,)

        try:
            establecimiento.save_to_db()
        except:
            return {'Error': "Un error ha ocurrido actualizando el establecimiento."}, 500

        return establecimiento.json(), 200
