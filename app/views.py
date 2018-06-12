import sys
sys.path.append("E:/Code/PublicationMS/app")
from flask import render_template , flash, redirect, request
from app import app
import retrieval


@app.route('/search', methods=['POST', 'GET'])
def search():
    option = request.values.get("optionsRadios")
    input_thing = request.values.get("input")
    result = retrieval.query_movie()
    return str()


@app.route('/')
@app.route('/index')
def index():
    return render_template("search.html")


@app.route('/greet')
def greet():
    return render_template("greeting.html")
