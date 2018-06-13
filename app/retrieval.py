import sys
#  公司电脑
# sys.path.append("E:/Code/PublicationMS/app")
sys.path.append("/Users/xingxiaofei/PycharmProjects/PublicationMS/app")
from sparql_tools import imdb_sparql, dbpedia_sparql, sparql_runner

"""
 负责检索功能实现的脚本
"""
def query_movie_by_name():
    query = """
PREFIX m: <http://data.linkedmdb.org/resource/movie/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT DISTINCT ?dir_name ?actor_name ?writer_name  WHERE {
  ?film rdfs:label "Lost in Translation";
        m:director ?dir;
        m:actor    ?actor;
        m:writer   ?writer.
        
       ?dir  m:director_name ?dir_name.
       ?actor m:actor_name   ?actor_name.
       ?writer m:writer_name ?writer_name.
}
"""
    return sparql_runner(imdb_sparql, query)


def query_director():
    query = """
        PREFIX m: <http://data.linkedmdb.org/resource/movie/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT ?filmTitle ?writer WHERE {
             ?film rdfs:label ?filmTitle.
             ?film m:director ?dir.
             ?film m:writer_name ?writer.
             ?film  m:director_name "Sofia Coppola".
            }
        """
    return sparql_runner(imdb_sparql, query)


def query_movie_by_director():
    query = """
   PREFIX m: <http://data.linkedmdb.org/resource/movie/>
   PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
   SELECT ?filmTitle ?actorName  ?producerName WHERE {
     ?film rdfs:label ?filmTitle;
        m:director ?dir;
        m:producer ?producer;
    
        m:actor ?actor.
     ?film m:director ?dir.
     ?dir  m:director_name "Sofia Coppola".
     ?actor m:actor_name ?actorName.
     ?producer m:producer_name ?producerName.   
}
    """
    return sparql_runner(imdb_sparql, query)
