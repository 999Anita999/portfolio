from flask import Flask
import random

app = Flask(__name__)


def make_h1(function):
    def wrapper():
        return '<h1>' + function() + '</h1>'
    return wrapper

@app.route("/")
@make_h1
def choose_number():
    return 'Choose a number between 1 and 10' \
            '<p><img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzB6MzJ2NnQ3bTEwMnhmaWh2dGk1amN0c2E2NXM5eWJsazNmbXJuMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TG3f7aaEnBsgMFQoPs/giphy.webp"></p>'


chosen_number = random.randint(1, 10)

@app.route("/<int:number>")
def guess_number(number):
    if number == chosen_number:
        return '<h1>You guessed the number!</h1>' \
               '<p><img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzB6MzJ2NnQ3bTEwMnhmaWh2dGk1amN0c2E2NXM5eWJsazNmbXJuMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TG3f7aaEnBsgMFQoPs/giphy.webp"></p>'

    elif number > chosen_number:
        return '<h1>Too high</h1>' \
               '<p><img src="">https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbWI2MXdsenZ6dzBveHc4OHlnMW5xNDBvMjRyeDFjNGFnaTFheGtqbiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/g3J4V7lbHNSCwH6FyP/giphy.webp</p>'
    else:
        return '<h1>Too low</h1>' \
               '<p><img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZzJyMmV5cnY4NHhldmh2cmpjNDZzZWl0aDV1eXY1dWFpMHM3dGRodiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ETA5Bt9ZaqPR1mLjzI/giphy.webp"></p>'



if __name__ == "__main__":
    app.run(debug=True)