from SPARQLWrapper import SPARQLWrapper, JSON

"""
    运行sparql查询的工具类
"""

imdb_sparql = SPARQLWrapper("http://data.linkedmdb.org/sparql")
dbpedia_sparql = SPARQLWrapper("http://dbpedia.org/sparql/")


# 运行查询语句的函数
def sparql_runner(sparql=dbpedia_sparql, query=''):
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    # 返回json数据
    return results