from db import db

class EstablecimientoModel(db.Model):
    __tablename__ = 'establecimientos'

    # Datos Principales
    id_establecimiento = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20))
    descripcion = db.Column(db.String(100))
    tipo_persona = db.Column(db.String(20))
    # Datos del Propieario
    propietario = db.Column(db.String(20))
    rfc = db.Column(db.String(20))
    telefono = db.Column(db.Integer)
    email = db.Column(db.String(30))
    # Domicilio del establecimiento
    calle = db.Column(db.String(20))
    colonia = db.Column(db.String(15))
    delegacion = db.Column(db.String(15))
    codigo_postal = db.Column(db.Integer)
    municipio = db.Column(db.String(15))
    # Datos del establecimiento
    superficie_construccion = db.Column(db.Integer)
    clave_catastral = db.Column(db.Integer)

    def __init__(self, nombre, descripcion, tipo_persona, propietario, rfc, telefono, email, calle, colonia, delegacion, codigo_postal, municipio, superficie_construccion, clave_catastral):
        self.nombre = nombre
        self.descripcion = descripcion
        self.tipo_persona = tipo_persona
        self.propietario = propietario
        self.rfc = rfc
        self.telefono = telefono
        self.email = email
        self.calle = calle
        self.colonia = colonia
        self.delegacion = delegacion
        self.codigo_postal = codigo_postal
        self.municipio = municipio
        self.superficie_construccion = superficie_construccion
        self.clave_catastral = clave_catastral
    
    def json(self):
        return {
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'tipo_persona': self.tipo_persona,
            'propietario': self.propietario,
            'rfc': self.rfc,
            'telefono': self.telefono,
            'email': self.email,
            'calle': self.calle,
            'colonia': self.colonia,
            'delegacion': self.delegacion,
            'codigo_postal': self.codigo_postal,
            'municipio': self.municipio,
            'superficie_construccion': self.superficie_construccion,
            'clave_catastral': self.clave_catastral
        }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(nombre=name).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()