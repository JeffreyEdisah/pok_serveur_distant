from flask_sqlalchemy import SQLAlchemy
import datetime

from app import app

db = SQLAlchemy(app)

class Commission(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    date = db.Column(db.Date, nullable=False)
    mail = db.Column(db.String(200), nullable=False)
    commission = db.Column(db.Text)

    def __init__(self,mail, commission):
        self.date = datetime.date.today()
        self.mail = mail
        self.commission = commission
    
db.create_all()
