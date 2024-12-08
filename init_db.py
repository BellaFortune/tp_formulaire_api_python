# import sqlite3

# connection = sqlite3.connect('app.db')

# with open('schema.sql') as f:
#     connection.executescript(f.read())

from app import app, db
from app.models import formulaires

def init_db():
    with app.app_context():
        # Supprimer toutes les tables existantes
        db.drop_all()
        
        # Créer de nouvelles tables
        db.create_all()
        
        print("Database initialized successfully!")

if __name__ == '__main__':
    init_db()
