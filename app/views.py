import sys
#  公司电脑
# sys.path.append("E:/Code/PublicationMS/app")
sys.path.append("/Users/xingxiaofei/PycharmProjects/PublicationMS/app")
from flask import render_template, redirect, request,make_response, jsonify
from app import app
import retrieval
import recommend
import data_visualization


@app.route('/search', methods=['POST', 'GET'])
def search():
    # 搜索范围判断条件
    option = request.values.get("optionsRadios")
    inputs = request.values.get("input")
    # data = retrieval.query_movie_by_name(inputs)
    # data = retrieval.query_movie_by_name(name=inputs)
    data = retrieval.query_book_by_name(name=inputs.replace(" ", "_"))
    recomendation = recommend.recommand_by_most_same(name=inputs.replace(" ", "_"))
    print("data type:", type(data))
    response = make_response(render_template("show_result.html",
                                             data=data, recomendation=recomendation, inputs=inputs))
    return response


@app.route('/')
@app.route('/index')
def index():
    data  = data_visualization.query_game_info()
    response = make_response(render_template("index.html", data = data))
    return response


@app.route('/greet')
def greet():
    return render_template("greeting.html")
