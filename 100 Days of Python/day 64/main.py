from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, SubmitField
from wtforms.validators import DataRequired
from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
import requests

API_KEY = 'afd039d914373f4892783511ca9fc098'

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhZmQwMzlkOTE0MzczZjQ4OTI3ODM1MTFjYTlmYzA5OCIsInN1YiI6IjY0ZDM2ZWFjZGI0ZWQ2MDBlMmI0ZWU4YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ZhT1McvkaY0bvkBEtmII9PsKsnwTv9Dq93WnGpDWhNc"
}

app = Flask(__name__)
db = SQLAlchemy()

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie-collection.db'
Bootstrap5(app)

db.init_app(app)


class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.Text, nullable=False)


with app.app_context():
    db.create_all()


class MyForm(FlaskForm):
    movie_rating = FloatField('Your Rating Out of 10',
                              validators=[DataRequired()])
    movie_review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Submit', validators=[DataRequired()])


class Movie_Add(FlaskForm):
    movie_title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Submit', validators=[DataRequired()])


@app.route("/", methods=["GET", "POST"])
def home():
    with app.app_context():
        data = Movies.query.order_by(Movies.rating).all()
    for i in range(len(data)):
        data[i].ranking = len(data) - i
    db.session.commit()
    return render_template("index.html", movie_data=data)


@app.route("/edit<int:id_num>", methods=['GET', 'POST'])
def edit(id_num):
    movie_form = MyForm()
    with app.app_context():
        result = db.session.execute(
            db.select(Movies).where(Movies.id == id_num)).scalar()
    if request.method == 'POST':
        with app.app_context():
            movie_to_update = db.session.execute(
                db.select(Movies).where(Movies.id == id_num)).scalar()
            movie_to_update.rating = movie_form.movie_rating.data
            movie_to_update.review = movie_form.movie_review.data
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie_edit=result, form=movie_form)


@app.route('/<int:id_num>', methods=['GET', 'POST'])
def delete(id_num):
    movie_id = id_num
    with app.app_context():
        result = db.session.execute(
            db.select(Movies).where(Movies.id == movie_id)).scalar()
        db.session.delete(result)
        db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=['GET', 'POST'])
def add():
    movie_add_form = Movie_Add()
    if movie_add_form.validate_on_submit():
        response = requests.get('https://api.themoviedb.org/3/search/movie', headers=headers,
                                params={'api_key': API_KEY, 'query': movie_add_form.movie_title.data})
        response.raise_for_status()
        response_data = response.json()["results"]
        return render_template('select.html', options=response_data)

    return render_template('add.html', form=movie_add_form)


@app.route('/select')  # type: ignore
def select():
    movie_api_id = request.args.get('id')
    if movie_api_id:
        response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_api_id}', headers=headers, params={
                                'api_key': API_KEY, "language": "en-US"})
        response.raise_for_status()
        response_data = response.json()
        new_movie = Movies(title=response_data['title'],
                           year=response_data['release_date'].split("-")[0],
                           description=response_data['overview'],
                           img_url=f"https://image.tmdb.org/t/p/original/{response_data['poster_path']}"
                           ) # type: ignore
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('edit', id_num=new_movie.id))

if __name__ == '__main__':
    app.run(debug=True)
