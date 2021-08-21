from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os

API_KEY = os.environ["API_KEY"]

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Movie(db.Model):
    __tablename__ = "Movie"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


db.create_all()


class RateMovieForm(FlaskForm):
    new_rating = StringField('Your Rating Out of 10 e.g. 7.5', validators=[DataRequired()])
    new_review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')


class AddMovieForm(FlaskForm):
    movie_title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')


@app.route("/")
def home():
    all_movies = db.session.query(Movie).order_by(Movie.rating).all()
    index = 0
    for num in range(len(all_movies), 0, -1):
        all_movies[index].ranking = num
        index += 1
    return render_template("index.html", movies=all_movies)


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    form = RateMovieForm()
    movie_id = request.args.get('id')
    movie_to_update = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie_to_update.rating = form.new_rating.data
        movie_to_update.review = form.new_review.data
        db.session.commit()
        return redirect('/')
    return render_template('edit.html', form=form, movie=movie_to_update)


@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect('/')


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie_to_search = form.movie_title.data
        parameters = {
            "api_key": API_KEY,
            "language": "en-US",
            "query": movie_to_search,
        }
        response = requests.get("https://api.themoviedb.org/3/search/movie", params=parameters)
        response.raise_for_status()
        results = response.json()
        return render_template('select.html', results=results["results"])
    return render_template('add.html', form=form)


@app.route('/select', methods=['GET', 'POST'])
def select():
    movie_id = request.args.get('id')
    parameters = {
        "api_key": API_KEY,
        "language": "en-US",
    }
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}", params=parameters)
    response.raise_for_status()
    results = response.json()
    title = results["original_title"]
    img_url = f"https://image.tmdb.org/t/p/w500{results['poster_path']}"
    year = results["release_date"][:4]
    description = results["overview"]
    new_movie = Movie(
        title=title,
        year=year,
        description=description,
        img_url=img_url
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit', id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
