from flask import Flask, render_template, request, redirect, url_for;

app = Flask(__name__)

@app.route("/")
def about():
    return render_template('about.html')

@app.route("/commissions",methods=["POST","GET"])
def commissions():
    return render_template("commissions.html")


@app.route("/commissions_sent",methods=["POST","GET"])
def send_commissions():
    mail = request.form.get("mail")
    commissions = request.form.get("commissions")
    if commissions == "":
        return redirect(url_for('commissions'))
    return redirect(url_for('commissions'))
