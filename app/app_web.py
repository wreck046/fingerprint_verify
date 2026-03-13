from flask import Flask, render_template, request

from services.verify_service import VerifyService
from infrastructure.database.user_repository import UserRepository
from infrastructure.scanner.simulator import SimulatorScanner


repo = UserRepository()
scanner = SimulatorScanner()

service = VerifyService(scanner, repo)


app = Flask(__name__)


@app.route("/", methods=["GET","POST"])
def dashboard():

    result = None

    if request.method == "POST":

        nik = request.form["nik"]

        result = service.verify(nik)

    return render_template("dashboard.html", result=result)


app.run()