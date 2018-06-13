from SPARQLWrapper import SPARQLWrapper,JSON

query_movie_dirBySofia = """
PREFIX m: <http://data.linkedmdb.org/resource/movie/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?filmTitle WHERE {
  ?film rdfs:label ?filmTitle.
  ?film m:director ?dir.
  ?dir  m:director_name "Sofia Coppola".
}
"""

def recommand_by_movie_name():
    sparql = SPARQLWrapper("http://data.linkedmdb.org/sparql")
    query = """
PREFIX m: <http://data.linkedmdb.org/resource/movie/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?filmTitle WHERE {
  ?film rdfs:label ?filmTitle.
  ?film m:director ?dir.
  ?dir  m:director_name WHERE {
    SELECT DISTINCT ?dir_name   WHERE {
         ?film rdfs:label "Lost in Translation";
               m:director ?dir.
              ?dir  m:director_name ?dir_name.
     }  
  }.
}

    """
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results