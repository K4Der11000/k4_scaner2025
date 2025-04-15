
from flask import Flask, render_template, request, redirect, url_for, send_file, Response
import subprocess
import os
from functools import wraps

app = Flask(__name__)
PASSWORD = "kader11000"

# Password protection
def check_auth(password):
    return password == PASSWORD

def authenticate():
    return Response('Authentication required.', 401, {'WWW-Authenticate': 'Basic realm="Login"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route("/", methods=["GET", "POST"])
@requires_auth
def index():
    return render_template("index.html")

@app.route("/scan", methods=["POST"])
@requires_auth
def scan():
    target = request.form.get("target")
    tool = request.form.get("tool")
    result = ""

    if not target:
        return "No target provided"

    if tool == "nikto":
        result = subprocess.getoutput(f"nikto -host {target}")
    elif tool == "nmap":
        result = subprocess.getoutput(f"nmap -sV --script vuln {target}")
    elif tool == "sublist3r":
        result = subprocess.getoutput(f"sublist3r -d {target} -o subdomains.txt")
        with open("subdomains.txt", "r") as f:
            result = f.read()
    elif tool == "dirb":
        result = subprocess.getoutput(f"dirb {target}")
    else:
        result = "Unknown tool"

    with open("last_scan.txt", "w") as f:
        f.write(result)

    # Convert results into a table
    rows = result.strip().split("
")

    return render_template("result.html", result=result, tool=tool, target=target, rows=rows)

@app.route("/download")
@requires_auth
def download():
    return send_file("last_scan.txt", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
