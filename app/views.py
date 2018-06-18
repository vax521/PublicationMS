import sys
#  公司电脑
# sys.path.append("E:/Code/PublicationMS/app")
sys.path.append("/Users/xingxiaofei/PycharmProjects/PublicationMS/app")
from flask import render_template, redirect, request, make_response
from app import app
import retrieval
import recommend
import data_visualization


@app.route('/search', methods=['POST', 'GET'])
def search():
    # 搜索范围判断条件
    option = request.values.get("optionsRadios")
    inputs = request.values.get("input")
    if option == 'option1':
        data = retrieval.query_book_by_name(name=inputs.replace(" ", "_"))
        recomendation = recommend.recommand_by_most_same(name=inputs.replace(" ", "_"))
    elif option == 'option2':
        data = retrieval.query_movie_by_name(name=inputs)
        recomendation = recommend.recommand_by_movie_name(name=inputs)
    else:
        data = retrieval.query_videogame_by_name(name=inputs.replace(" ", "_"))
        recomendation = recommend.recommand_by_most_same(name=inputs.replace(" ", "_"))

    response = make_response(render_template("show_result.html",
                                             data=data, recomendation=recomendation, inputs=inputs))
    return response


@app.route('/')
@app.route('/index')
def index():
    data = data_visualization.query_game_info()
    response = make_response(render_template("index.html", data=data))
    return response


@app.route('/greet')
def greet():
    return render_template("greeting.html")
