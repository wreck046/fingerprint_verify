from flask import Flask, jsonify
from infrastructure.scanner.scanner import FingerprintScanner
from infrastructure.scanner.simulator import SimulatorScanner

app = Flask(__name__)

try:
    scanner = FingerprintScanner()
    mode = "hardware"
except:
    scanner = SimulatorScanner()
    mode = "simulator"


@app.route("/status")
def status():

    return jsonify({
        "status": "running",
        "scanner_mode": mode
    })


@app.route("/scan")
def scan():

    try:

        template = scanner.capture()

        return jsonify({
            "success": True,
            "template": template.hex()
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        })


app.run(host="0.0.0.0", port=5001)