import sys
#  公司电脑
# sys.path.append("E:/Code/PublicationMS/app")
sys.path.append("/Users/xingxiaofei/PycharmProjects/PublicationMS/app")
from sparql_tools import imdb_sparql, dbpedia_sparql, sparql_runner


def get_all_author_num():
    """
    查询作者的数量
    返回结果为dict类型，
    {'callret-0': {'type': 'typed-literal', 'datatype': 'http://www.w3.org/2001/XMLSchema#integer', 'value': '32512'}}
    """
    query ="""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX dbp: <http://dbpedia.org/property/>
        SELECT COUNT(?author)
            WHERE {
            ?author rdf:type dbo:Writer.
        }
        """
    return sparql_runner(dbpedia_sparql, query)

def get_notablework_num():
    """
   查询著名作品的数量
    返回结果为dict类型，
    """
    query = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX dbo: <http://dbpedia.org/ontology/>
    PREFIX dbp: <http://dbpedia.org/property/>
    SELECT  COUNT(?work)
    WHERE {
        ?author rdf:type dbo:Writer.
        ?author dbo:notableWork ?work.
    } 
    """



