from app import db
from datetime import date


class formulaires(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    nom_du_bootcamp = db.Column(db.String(length=30), nullable=False)
    priorite_de_retour = db.Column(db.String(length=30), nullable=False)
    type_de_retour = db.Column(db.String(length=30), nullable=False)
    dates = db.Column(db.Date(), nullable=False)
    evaluation = db.Column(db.Integer(), nullable=False)
    commentaire = db.Column(db.String(length=1024), nullable=True)
    piece_joites = db.Column(db.String(length=255), nullable=True)
    droits_donnee = db.Column(db.Boolean(), default=False)

    def __repr__(self):
        return f'Formulaire {self.id}: {self.nom_du_bootcamp}'