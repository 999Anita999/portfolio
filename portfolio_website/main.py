from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, request


app = Flask(__name__)

this_year = date.today().year


@app.route("/")
def home_page():
    return render_template('index.html', this_year=this_year)


@app.route("/portfolio")
def portfolio():
    return render_template('portfolio.html', this_year=this_year)

@app.route("/experience")
def experience():
    return render_template('experience.html', this_year=this_year)

@app.route("/travel")
def travel():
    return render_template('travel.html', this_year=this_year)

@app.route("/projects")
def projects():
    return render_template('projects.html', this_year=this_year)

@app.route("/chiefs")
def chiefs():
    return render_template('chiefs.html', this_year=this_year)


if __name__ == "__main__":
    app.run(debug=True)
