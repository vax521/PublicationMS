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


# 处理查询模块返回的dict数据，一对多的字典
def show_result_processing(results):
    finished_product = {}
    for item in results['head']['vars']:
        a = set()
        for row in results['results']['bindings']:
            a.add(row[item]['value'])
        finished_product[item] = a
    return finished_product


# 处理 推荐模块返回的dict数据，只抽取 label 字段
def recommand_result_processing(results):
    recommands=[]
    for result in results["results"]["bindings"]:
            recommands.append(result['label']['value'])
    return recommands


#  处理数据可视化模块的数据 返回 value类型为list的字典
def result_to_dict(results={}):
    finished_product = {}
    for item in results['head']['vars']:
        a = []
        for row in results['results']['bindings']:
            a.append(row[item]['value'])
        finished_product[item] = a
    return finished_product