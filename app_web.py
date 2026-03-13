from flask import Flask, render_template, request
from services.fingerprint_service import verify_user

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def dashboard():

    result = None

    if request.method == "POST":

        nik = request.form["nik"]

        result = verify_user(nik)

    return render_template("dashboard.html", result=result)

app.run(port=5000)