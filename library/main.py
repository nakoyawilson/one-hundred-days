from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


db.create_all()


@app.route("/")
def home():
    all_books = db.session.query(Book).all()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        rating = request.form["rating"]
        book = Book(title=title, author=author, rating=rating)
        db.session.add(book)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add.html')


@app.route("/edit", methods=["GET", "POST"])
def edit():
    book_id = request.args.get('id')
    book_to_update = Book.query.get(book_id)
    if request.method == "POST":
        new_rating = request.form["new_rating"]
        book_to_update.rating = new_rating
        db.session.commit()
        return redirect('/')
    else:
        return render_template('edit.html', book=book_to_update)


@app.route("/delete")
def delete():
    book_id = request.args.get('id')
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)

