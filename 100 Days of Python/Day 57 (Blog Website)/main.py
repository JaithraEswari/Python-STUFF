from urllib import response
from flask import Flask, render_template
import requests

app = Flask(__name__)

url = 'https://api.npoint.io/c790b4d5cab58020d391'
response = requests.get(url).json()

@app.route('/blog')
def home():
    return render_template("index.html", blog_data = response)

@app.route('/post/<int:id_num>')
def each_post(id_num):
    return render_template("post.html", posts=response, ID=id_num)

if __name__ == "__main__":
    app.run(debug=True)
