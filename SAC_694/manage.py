import bcrypt
from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////path/to/database.db'
db = SQLAlchemy(app)

# Create user model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    encrypted_password = db.Column(db.String, nullable=False)

    # Encrypt password when creating user
    def __init__(self, username, password):
        self.username = username
        self.encrypted_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Login route
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    user = User.query.filter_by(username=username).first()

    # Compare encrypted password
    if bcrypt.checkpw(password.encode('utf-8'), user.encrypted_password):
        # Password matches
        return redirect('/home')
    else:
        # Password does not match
        return render_template('login.html', error="Incorrect username or password")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)