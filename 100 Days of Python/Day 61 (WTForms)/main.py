from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import InputRequired, Email, Length
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.secret_key = 'secret'

bootstrap = Bootstrap5(app)


class MyForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email address.')])
    password = PasswordField('password', validators=[InputRequired(), Length(min= 8, message='Field must be at least 8 characters')])
    submit = SubmitField('submit', validators=[InputRequired()])


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = MyForm()
    if login_form.validate_on_submit():
        if login_form.email.data == 'admin@email.com' and login_form.password.data == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
