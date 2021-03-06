from flask import Flask
from random import randint

app = Flask(__name__)
rand = randint(0, 9)
@app.route("/")
def main():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">' \
           '<p>Add /n in the url where n is your guessed number then hit enter</p>'


@app.route("/<int:number>")
def random_number(number):

    if rand == number:
        return '<h1 style="color:green">You got it right!</h1>' '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'

    elif rand > number:
        return '<h1 style="color:blue">Too Low</h1>' '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'

    else:
        return '<h1 style="color:red">Too High</h1>' '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)

