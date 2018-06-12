from SPARQLWrapper import SPARQLWrapper,JSON


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


def query_movie():
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
    # all_movie = []
    # for result in results["results"]["bindings"]:
    #    all_movie.append(result)
    return results