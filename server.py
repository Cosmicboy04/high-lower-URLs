from flask import Flask
import random

random_number = random.randint(0, 20)
print(random_number)

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>" \
           "<p>Go to /rules to read the rules</p>"


@app.route('/rules')
def rules():
    return "<h1>Type in the URL section your guess | e.g: 127.0.0.1:5000/2</h1>"


@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o7abAHdYvZdBNnGZq/giphy.gif'/>"


    elif guess < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/pVBUBqNdTdsVuiybM4/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


@app.route("/secret-area")
def secret():
    return f"The number is {random_number}"


if __name__ == "__main__":
    app.run(debug=True)
