from flask import Flask, render_template
import requests
from datetime import date

app = Flask(__name__)
today = date.today()

data = requests.get('https://api.npoint.io/741a5256889503b144f3').json()
d1 = today.strftime("%B %d, %Y")

@app.route('/')
def index():
    return render_template('index.html', posts = data, date = d1)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:id_num>')
def post(id_num):
    return render_template('post.html', posts = data, ID=id_num, date = d1 )

if __name__ == '__main__':
    app.run(debug=True)