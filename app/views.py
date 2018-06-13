import sys
#  公司电脑
# sys.path.append("E:/Code/PublicationMS/app")
sys.path.append("/Users/xingxiaofei/PycharmProjects/PublicationMS/app")
from flask import render_template, redirect, request,make_response, jsonify
from app import app
import retrieval
import recommend


@app.route('/search', methods=['POST', 'GET'])
def search():
    # 搜索范围判断条件
    option = request.values.get("optionsRadios")
    input_thing = request.values.get("input")
    # data = retrieval.query_movie_by_name()
    data = retrieval.query_movie_by_name()
    recomendation = recommend.recommand_by_movie_name(name="Sofia Coppola")
    print("data type:", type(data))
    response = make_response(render_template("show_result.html", data=data, recomendation=recomendation))
    return response


@app.route('/')
@app.route('/index')
def index():
    return render_template("search.html")


@app.route('/greet')
def greet():
    return render_template("greeting.html")
