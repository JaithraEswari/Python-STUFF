from flask import Flask, render_template, request
import requests
from datetime import date
from smtplib import SMTP

my_email = 'ejljaithra2002@gmail.com'
my_password = 'xxxxxxxxx'

app = Flask(__name__)
today = date.today()

data = requests.get('https://api.npoint.io/741a5256889503b144f3').json()
d1 = today.strftime("%B %d, %Y")

@app.route('/')
def index():
    return render_template('index.html', posts = data, date = d1)

@app.route('/about', methods=['GET','POST'])
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        with SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(my_email, my_password)
            connection.sendmail(my_email, 'ejljaithra2002@gmail.com', f'Subject: New Message\n\nName: {request.form["name"]}\nEmail: {request.form["email"]}\nPhone: {request.form["phone"]}\nMessage: {request.form["message"]}')
        return render_template('contact.html', msg_sent = True)
    else:
        return render_template('contact.html', msg_sent = False)

@app.route('/post/<int:id_num>')
def post(id_num):
    return render_template('post.html', posts = data, ID=id_num, date = d1 )

if __name__ == '__main__':
    app.run(debug=True)