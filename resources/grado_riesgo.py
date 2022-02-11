from flask_restful import Resource
from models.grado_riesgo import RiesgoModel
from flask import request


class Riesgo(Resource):
    
    def post(self):
        request_data = request.get_json()

        # try:
        #     id_riesgo = request_data['id_riesgo']

        #     if RiesgoModel.find_by_id(id_riesgo):
        #         return {'Error': "Una evaluacion de grado de riesgos con ID '{}' ya existe.".format(id_riesgo)}, 400
        # except:
        #     print("ID no encontrada, creando nueva evaluacion")
         
        grado_riesgo = RiesgoModel(**request_data,)

        try:
            grado_riesgo.save_to_db()
        except:
            return {'Error': "Un error ocurrio insertando los datos."}, 500

        return grado_riesgo.json(), 201

    def put(self):
        request_data = request.get_json()
        # name = request_data['nombre']
        # exist = RiesgoModel.find_by_id(id_riesgo)

        # if exist:
        #     exist.delete_from_db()

        riesgo = RiesgoModel(**request_data,)

        try:
            riesgo.save_to_db()
        except:
            return {'Error': "Un error ha ocurrido actualizando la autoevaluacion."}, 500

        return riesgo.json(), 200
