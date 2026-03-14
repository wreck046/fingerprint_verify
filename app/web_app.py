from flask import Flask, render_template, request
from infrastructure.database.user_repository import UserRepository

app = Flask(__name__)
repo = UserRepository()

@app.route("/")
def dashboard():
    users = repo.get_all_users()
    logs = repo.get_logs()
    return render_template("dashboard.html", users=users, logs=logs)

@app.route("/enroll", methods=["POST"])
def enroll():
    name = request.form["name"]
    nik = request.form["nik"]

    repo.create_user(name, nik)

    return "User created"

app.run()