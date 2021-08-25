from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


def create_cafe_dictionary(cafe):
    """Converts cafe object to dictionary"""
    cafe_dictionary = cafe.__dict__
    del cafe_dictionary['_sa_instance_state']
    return cafe_dictionary


@app.route("/")
def home():
    return render_template("index.html")
    

# HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    all_cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(all_cafes)
    cafe_dict = create_cafe_dictionary(random_cafe)
    return jsonify(cafe=cafe_dict)


@app.route("/all")
def get_all_cafes():
    all_cafes = db.session.query(Cafe).all()
    cafes_list = [create_cafe_dictionary(cafe) for cafe in all_cafes]
    return jsonify(cafes=cafes_list)


@app.route("/search")
def search_for_cafes():
    location = request.args.get("loc").title()
    results = Cafe.query.filter_by(location=location).all()
    results_list = [create_cafe_dictionary(result) for result in results]
    error = {"Not Found": "Sorry, we don't have a cafe at that location."}
    if len(results_list) == 0:
        return jsonify(error=error)
    elif len(results_list) == 1:
        return jsonify(cafe=results_list)
    else:
        return jsonify(cafes=results_list)


# HTTP POST - Create Record
@app.route("/add", methods=["GET", "POST"])
def add_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        has_sockets=bool(request.form.get("has_sockets")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    success = {
        "success": "Successfully added the new cafe."
    }
    return jsonify(response=success)


# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
