from db import db

class TramiteModel(db.Model):
    __tablename__ = 'tramites'

    folio = db.Column(db.Integer, primary_key=True)
    tramite = db.Column(db.String(20))
    inicio_tramite = db.Column(db.Date)
    estatus = db.Column(db.String(20))
    estatus_archivos = db.Column(db.String(20))
    comentarios = db.Column(db.String(100))
    costo = db.Column(db.Float(precision=2))

    usuario_fk = db.Column(db.Integer)
    establecimiento_fk = db.Column(db.Integer)

    # usuario_fk = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    # usuario = db.relationship('UsuarioModel')

    # establecimiento_fk = db.Column(db.Integer, db.ForeignKey('establecimiento.id'))
    # establecimiento = db.relationship('EstablecimientoModel')

    def __init__(self, tramite, inicio_tramite, estatus, estatus_archivos, comentarios, costo, usuario_fk, establecimiento_fk):
        self.tramite = tramite
        self.inicio_tramite = inicio_tramite
        self.estatus = estatus
        self.estatus_archivos = estatus_archivos
        self.comentarios = comentarios
        self.costo = costo
        self.usuario_fk = usuario_fk
        self.establecimiento_fk = establecimiento_fk

    def json(self):
        return {
            'tramite': self.tramite,
            'inicio_tramite': self.inicio_tramite,
            'estatus': self.estatus,
            'estatus_archivos': self.estatus_archivos,
            'comentarios': self.comentarios,
            'costo': self.costo,
            'usuario_fk': self.usuario_fk,
            'establecimiento_fk': self.establecimiento_fk
        }

    @classmethod
    def find_by_user(cls, user):
        return cls.query.filter_by(usuario_fk=user).all()