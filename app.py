from flask import Flask, render_template, request, flash, redirect, url_for, session
from datetime import timedelta, date
import os
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 
app.permanent_session_lifetime = timedelta (minutes=60)

app.config['SQLALCHEMY_DATABASE_URI'] = 

db = SQLAlchemy(app)
migrate = Migrate(app,db)
db.init_app(app)

class Commissions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default = date.today())
    mail = db.Column(db.String(200), nullable=False)
    commission = db.Column(db.Text, nullable=False)

    def __init__(self,mail,commission):
        self.mail = mail
        self.commission = commission
        

with app.app_context():
    db.create_all()

@app.route("/")
def about():
    return render_template('about.html')

@app.route("/commissions",methods=["POST","GET"])
def commissions():
    if request.method == "POST":
        session.permanent = True
        cmail = request.form.get("mail")
        session["mail"] = cmail
        ccommission = request.form.get("commissions")
        if commissions == "":
            flash("Entrez une commission valide", "error")
            return redirect(url_for('commissions'))
        else:
            found_commission = Commissions.query.filter_by(mail=cmail).first()
            if found_commission:
                session["mail"] = found_commission.mail
            else:
                com = Commissions(cmail, ccommission)
                db.session.add(com)
                db.session.commit()
            return redirect(url_for('commissions'))
    else :
        return render_template("commissions.html")

if __name__ == "__main__":
    app.run()