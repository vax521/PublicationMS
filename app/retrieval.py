from SPARQLWrapper import SPARQLWrapper,JSON


"""
 负责检索功能实现的脚本
"""


def query_movie_by_name():
    sparql = SPARQLWrapper("http://data.linkedmdb.org/sparql")
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
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results


def query_director():
    sparql = SPARQLWrapper("http://data.linkedmdb.org/sparql")
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
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    all_movie = []
    for result in results["results"]["bindings"]:
        all_movie.append(result)
    return all_movie


def query_movie_by_director():
    sparql = SPARQLWrapper("http://data.linkedmdb.org/sparql")
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
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    # print(type(results)) 字典类型
    # all_movie = []
    # for result in results["results"]["bindings"]:
    #    all_movie.append(result)
    return results
