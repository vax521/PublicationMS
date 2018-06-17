import sys
#  公司电脑
# sys.path.append("E:/Code/PublicationMS/app")
sys.path.append("/Users/xingxiaofei/PycharmProjects/PublicationMS/app")
from sparql_tools import *

"""
 负责检索功能实现的脚本
"""


def query_movie_by_name(name=''):
    query = """
        PREFIX m: <http://data.linkedmdb.org/resource/movie/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX dc: <http://purl.org/dc/terms/>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        SELECT  ?dir_name ?actor_name ?writer_name ?date ?runtime ?page WHERE {
          ?film rdfs:label '"""+name+"""';
                m:director ?dir;
                m:actor    ?actor;
                m:writer   ?writer;
                dc:date    ?date;
                m:runtime  ?runtime;
                foaf:page   ?page.
                
               ?dir  m:director_name ?dir_name.
               ?actor m:actor_name   ?actor_name.
               ?writer m:writer_name ?writer_name.
        }
        """
    print("检索语句")
    print(query)
    results = sparql_runner(imdb_sparql, query)
    result_processed = show_result_processing(results)
    return result_processed


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


def query_book_by_name(name=""):
    query = """
   SELECT ?thumbnail ?author ?kind ?country ?language ?comment ?links
    WHERE {
    dbr:"""+name+""" dbp:title ?title;
           dbo:thumbnail ?thumbnail;
           dbp:author ?author;
           dbo:literaryGenre ?literaryGenre;
           dbp:country ?country;
           dbp:language ?language;
           rdfs:comment ?comment;
           dbo:wikiPageExternalLink ?links.
    ?literaryGenre rdfs:label ?kind.   
     FILTER(LANG(?kind)="zh" && LANG(?comment)="zh")
    }
    """
    print("书籍查询语句：")
    print(query)
    results = sparql_runner(dbpedia_sparql, query)
    result_processed = show_result_processing(results)
    return result_processed
