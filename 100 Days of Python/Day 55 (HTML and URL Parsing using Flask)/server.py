from flask import Flask
import random

app = Flask(__name__)

@app.route('/URL/')
def a_function():
    return  '<h1>Guess a number between 0 and 9</h1>'\
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route('/URL/<value>') # type: ignore
def b_function(value):
    random_number = random.randint(0,10)
    if random_number < int(value):
        return  '<h1>Too High</h1>'\
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    elif random_number > int(value):
        return  '<h1>Too Low</h1>'\
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif random_number == int(value):
        return  '<h1>Correct</h1>'\
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


if __name__ == '__main__':
   app.run(debug=True)
