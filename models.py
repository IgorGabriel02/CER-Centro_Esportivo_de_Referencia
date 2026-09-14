from flask_sqlalchemy import SQLAlchemy


# CREATE SQL OBJECT


db = SQLAlchemy()

# TABLES

class user(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(100) , nullable=False)
    email = db.Column(db.String(100) , nullable=False)
    senha = db.Column(db.String(20), nullable=False) 
    

