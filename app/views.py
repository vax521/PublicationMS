from flask import render_template , flash, redirect
from app import app


@app.route('/')
@app.route('/search')
def search():
    return render_template("search.html")


@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/greet')
def greet():
    return render_template("greeting.html")