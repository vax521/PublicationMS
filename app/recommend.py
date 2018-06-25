import sys
#  公司电脑
sys.path.append("E:/Code/PublicationMS/app")
# sys.path.append("/Users/xingxiaofei/PycharmProjects/PublicationMS/app")
from sparql_tools import *

query_movie_dirBySofia = """
PREFIX m: <http://data.linkedmdb.org/resource/movie/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?filmTitle WHERE {
  ?film rdfs:label ?filmTitle.
  ?film m:director ?dir.
  ?dir  m:director_name "Sofia Coppola".
}
"""

query_movie_by_movie = """
PREFIX m: <http://data.linkedmdb.org/resource/movie/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?filmTitle WHERE {
    ?film rdfs:label ' '.
    ?film m:director ?director.
    ?director m:made ?other_movie.
    ?other_movie m:label ?filmTitle.
    FILTER(?filmTitle!='') 
}
LIMIT 3
"""


# 通过字符串拼接传参数，需要加单引号
# def recommand_by_movie_name(name=""):
#     query = """
# PREFIX m: <http://data.linkedmdb.org/resource/movie/>
# PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
# SELECT ?filmTitle WHERE {
#   ?film rdfs:label ?filmTitle.
#   ?film m:director ?dir.
#   ?dir  m:director_name '"""+name+"""'.
# } LIMIT 3
#     """
#     # print(query)
#     return sparql_runner(imdb_sparql, query)

def recommand_by_movie_name(name=""):
    """
    推荐电影导演的其他作品
    :param name:
    :return:
    """
    query = """
       PREFIX m: <http://data.linkedmdb.org/resource/movie/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX foaf:  <http://xmlns.com/foaf/0.1/>
        SELECT ?filmTitle  WHERE {
            ?film rdfs:label '"""+name+"""'.
            ?film m:director ?director.
            ?director foaf:made ?other_movie.
            ?other_movie rdfs:label ?filmTitle.
            FILTER(?filmTitle != '"""+name+"""') 
        }
        LIMIT 3
    """
    print("电影推荐语句：")
    print(query)
    results = sparql_runner(imdb_sparql, query)
    print("电影推荐结果：")
    results_processed = {}
    for result in results["results"]["bindings"]:
        print(result['filmTitle']['value'])
        results_processed[result['filmTitle']['value']] = ""
    return results_processed


def recommand_by_most_same(name=""):
    """
     基于数据相似性的推荐
    :param name: 资源名
    :return:
    """
    query = """
     SELECT   ?name ?abstract
     WHERE {
         dbr:"""+name+""" dct:subject ?o.
         ?movie dct:subject ?o.
         ?movie rdfs:label ?name.
         ?movie dbo:abstract ?abstract.
         FILTER(?movie != dbr:"""+name+""" && LANG(?abstract)="zh" && LANG(?name)="zh").
    }
    GROUP BY ?movie ?name ?abstract
    ORDER BY DESC(COUNT(?movie))
    LIMIT 3
    """
    print("推荐语句：")
    print(query)
    results = sparql_runner(dbpedia_sparql, query)
    recommands = recommand_result_processing(results)
    return recommands