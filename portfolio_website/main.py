from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap



app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
