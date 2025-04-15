
from flask import Flask, request, redirect, url_for, render_template_string, session
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'supersecretkey'
csrf = CSRFProtect(app)
PASSWORD_HASH = generate_password_hash("kader11000")

def check_password(password):
    return check_password_hash(PASSWORD_HASH, password)

@app.before_request
def before_request():
    if 'logged_in' not in session and request.endpoint != 'login':
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form.get('password')
        if check_password(password):
            session['logged_in'] = True
            return redirect(url_for('home'))
        else:
            return "Incorrect password!"
    return render_template_string('''
    <form action="/login" method="POST">
        <h2>Login to Access</h2>
        <input type="password" name="password" placeholder="Enter password" required>
        <input type="submit" value="Login">
    </form>
    ''')

@app.route('/')
def home():
    return "Welcome to the Vulnerability Scanner Interface!"

if __name__ == "__main__":
    app.run(debug=True, ssl_context='adhoc')
