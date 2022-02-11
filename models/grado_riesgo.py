from db import db

# Atento a el nombre de la clase y el archivo
class RiesgoModel(db.Model):
    __tablename__ = 'riesgos'

    id_riesgo = db.Column(db.Integer, primary_key=True)
    altura_maxima = db.Column(db.String(15))
    superficie_total = db.Column(db.String(25))
    liquidos_inflamables = db.Column(db.String(25))
    materiales_explosivos = db.Column(db.String(2)) #Opcion a bool
    sustancias_quimicas = db.Column(db.String(27))
    servicio_gas = db.Column(db.String(25))
    total_personas = db.Column(db.String(22))
    gases_inflamables = db.Column(db.String(28))
    materiales_alta_combustion = db.Column(db.String(28))
    voltaje_electrico = db.Column(db.String(22))
    proteccion_personal = db.Column(db.String(28))
    caracteristicas_cristales = db.Column(db.String(55))
    escaleras = db.Column(db.String(52))
    inmuebles_alta_combustion = db.Column(db.String(2))  #Opcion a bool

    def __init__(self, altura_maxima, superficie_total, liquidos_inflamables, materiales_explosivos, sustancias_quimicas, servicio_gas, total_personas, gases_inflamables, materiales_alta_combustion, voltaje_electrico, proteccion_personal, caracteristicas_cristales, escaleras, inmuebles_alta_combustion):
        self.altura_maxima = altura_maxima
        self.superficie_total = superficie_total
        self.liquidos_inflamables = liquidos_inflamables
        self.materiales_explosivos = materiales_explosivos
        self.sustancias_quimicas = sustancias_quimicas
        self.servicio_gas = servicio_gas
        self.total_personas = total_personas
        self.gases_inflamables = gases_inflamables
        self.materiales_alta_combustion = materiales_alta_combustion
        self.voltaje_electrico = voltaje_electrico
        self.proteccion_personal = proteccion_personal
        self.caracteristicas_cristales = caracteristicas_cristales
        self.escaleras = escaleras
        self.inmuebles_alta_combustion = inmuebles_alta_combustion
    
    def json(self):
        return {
            'altura_maxima': self.altura_maxima,
            'superficie_total': self.superficie_total,
            'liquidos_inflamables': self.liquidos_inflamables,
            'materiales_explosivos': self.materiales_explosivos,
            'sustancias_quimicas': self.sustancias_quimicas,
            'servicio_gas': self.servicio_gas,
            'total_personas': self.total_personas,
            'gases_inflamables': self.gases_inflamables,
            'materiales_alta_combustion': self.materiales_alta_combustion,
            'voltaje_electrico': self.voltaje_electrico,
            'proteccion_personal': self.proteccion_personal,
            'caracteristicas_cristales': self.caracteristicas_cristales,
            'escaleras': self.escaleras,
            'inmuebles_alta_combustion': self.inmuebles_alta_combustion
        }
    
    @classmethod
    def find_by_id(cls, id_riesgo):
        return cls.query.filter_by(id_riesgo=id_riesgo).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()