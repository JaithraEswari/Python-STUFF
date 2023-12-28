from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
import requests

app = Flask(__name__)
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'

db.init_app(app)


class Books(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String)
    rating: Mapped[int] = mapped_column(Float)


with app.app_context():
    db.create_all()


@app.route('/', methods=['GET'])
def home():
    with app.app_context():
        result = Books.query.all()
    return render_template('index.html', books=result)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        with app.app_context():
            new_book = Books(
                title=request.form['title'], author=request.form['author'], rating=request.form['rating'])  # type: ignore
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route('/edit?id=<int:id_num>', methods=['GET', 'POST'])
def edit(id_num):
    with app.app_context():
        result = db.session.execute(
            db.select(Books).where(Books.id == id_num)).scalar()
    if request.method == 'POST':
        with app.app_context():
            book_to_update = db.session.execute(
                db.select(Books).where(Books.id == id_num)).scalar()
            book_to_update.rating = request.form['new_rating']
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', books_edit=result)


@app.route('/id=<int:id_num>', methods=['GET', 'POST'])
def delete(id_num):
    book_id = id_num
    with app.app_context():
        book_to_delete = db.session.execute(
            db.select(Books).where(Books.id == book_id)).scalar()
        db.session.delete(book_to_delete)
        db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
