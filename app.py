from flask import Flask, render_template, request, redirect, url_for, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 
app.permanent_session_lifetime = timedelta (minutes=60)

@app.route("/")
def about():
    return render_template('about.html')

@app.route("/commissions",methods=["POST","GET"])
def commissions():
    if request.method == "POST" and "commissions" not in session:
        session.permanent = True
        mail = request.form.get("mail")
        session["mail"] = mail
        commissions = request.form.get("commissions")
        session["commissions"] = commissions
        if commissions == "":
            flash("Entrez une commission valide")
            return redirect(url_for('commissions'))
        return redirect(url_for('commissions'))
    else :
        return render_template("commissions.html")

