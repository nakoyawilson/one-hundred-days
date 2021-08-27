from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
# Line below only required once, when creating DB.
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user_name = request.form["name"]
        password = generate_password_hash(request.form["password"], method='pbkdf2:sha256', salt_length=8)
        email = request.form["email"]
        if User.query.filter_by(email=email).first():
            flash("You've already signed up with that email, log in instead!")
            return redirect("/register")
        else:
            new_user = User(
                name=user_name,
                email=email,
                password=password,
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect("/secrets")
    else:
        return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(email=request.form["email"]).first()
        password = request.form["password"]
        if not user:
            flash('That email does not exist, please try again.')
            return redirect("/login")
        else:
            password_hash = user.password
            if check_password_hash(password_hash, password):
                login_user(user)
                return redirect("/secrets")
            else:
                flash('Incorrect password, please try again.')
                return redirect("/login")
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/download')
@login_required
def download():
    return send_from_directory(directory="static", path="files/cheat_sheet.pdf")


@login_manager.user_loader
def load_user(id):
    return User.query.get(id)


if __name__ == "__main__":
    app.run(debug=True)
