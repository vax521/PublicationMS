from SPARQLWrapper import SPARQLWrapper,JSON


def recommand_by_movie_name():
    sparql = SPARQLWrapper("http://data.linkedmdb.org/sparql")
    query = """
    PREFIX m: <http://data.linkedmdb.org/resource/movie/>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT COUNT(?movie) SAMPLE(?movie) WHERE {
      ?film rdfs:label "Lost in Translation";
            rdf:type ?o.

    
    }
    """
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results