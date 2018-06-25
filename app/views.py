import sys
#  公司电脑
sys.path.append("E:/Code/PublicationMS/app")
# sys.path.append("/Users/xingxiaofei/PycharmProjects/PublicationMS/app")
from flask import render_template, request, make_response, Response
import json
from app import app
import retrieval
import recommend
from data_visualization import *


class MyResponse(Response):
    @classmethod
    def force_type(cls, rv, environ=None):
        if isinstance(rv, dict):
            rv = jsonify(rv)
        return super(MyResponse, cls).force_type(rv, environ)


# Turn sets into lists before serializing, or use a custom default handler to do so:
def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError


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
    response = make_response(render_template("index.html"))
    return response


@app.route('/get_book_info')
def get_book_info():
    result = dict()
    result['nationality'] = get_writer_nationality()
    result['notablework'] = get_notablework_num()
    print(result)
    # print(Response(result, mimetype='application/json'))
    return json.dumps(result, default=set_default)


@app.route('/get_movie_info')
def get_movie_info():
    result = dict()
    result['country_movies'] = get_country_movies()
    result['director_movies'] = get_director_movies()
    print(result)
    # print(Response(result, mimetype='application/json'))
    return json.dumps(result, default=set_default)

