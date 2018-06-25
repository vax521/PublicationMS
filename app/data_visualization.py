import sys
#  公司电脑
sys.path.append("E:/Code/PublicationMS/app")
# sys.path.append("/Users/xingxiaofei/PycharmProjects/PublicationMS/app")
from sparql_tools import *

"""
 负责为可视化页面提供数据的脚本
"""


def json_to_dict(results=""):
    """
    返回值处理函数
    :param results:
    :return: dict类型
    """
    finished_product = {}
    for item in results['head']['vars']:
        a = []
        for row in results['results']['bindings']:
            a.append(row[item]['value'])
        finished_product[item] = a
    return finished_product


"""
  书籍信息统计部分
"""


def get_all_author_num():
    """
    查询所有作者的数量
    返回结果为dict类型:{'auhtor_name':['32512']}
    """
    query ="""
        SELECT COUNT(?author) AS ?author_number
            WHERE {
            ?author rdf:type dbo:Writer.
        }
        """
    results =  sparql_runner(dbpedia_sparql, query)
    author_number = json_to_dict(results)
    return author_number


def get_writer_gender():
    """
     获取所有的作家的性别信息
    # 姓名：foaf:name ?name;
    # 性别：foaf:gender
    :return:dict
    """
    query_writers_gender = """
    SELECT   ?gender COUNT(?gender) AS ?gender_nums 
     WHERE {
     ?author rdf:type dbo:Writer;
             foaf:name ?name;
             foaf:gender ?gender.
     }
     GROUP BY ?gender
    """
    print("获取所有的作家性别信息:")
    print(query_writers_gender)
    results = sparql_runner(dbpedia_sparql, query_writers_gender)
    return show_result_processing(results)


def get_writer_nationality():
    """
     获取作家数量前10的国家
    # 姓名：foaf:name ?name;
    # 性别：foaf:gender
    :return:dict
    """
    query_writers_nationality = """
    SELECT   ?nationality COUNT(?author) AS ?author_nums 
     WHERE {
     ?author rdf:type dbo:Writer;
             dbp:nationality ?nationality.
     }
     GROUP BY ?nationality
     ORDER BY DESC(COUNT(?author))
     LIMIT 10
    """
    print("获取所有的作家国别信息:")
    print(query_writers_nationality)
    results = sparql_runner(dbpedia_sparql, query_writers_nationality)
    return show_result_processing(results)


def get_notablework_num():
    """
    查询拥有著名作品的作者和著名作品的数量 前十名
    返回结果为dict类型，作者名及其对应的著名作品数量
    {'author_name': ['Julian Stockwin', 'Marcus Tullius Cicero', 'OBE', "Edna O'Brien", 'Vince Powell', '(OBE)', 'Roy Clarke', 'John Banville', 'David Mamet', 'Edward Stratemeyer'],
      'work_nums': ['16', '15', '14', '14', '14', '13', '13', '12', '12', '12']}
    """
    query = """
    SELECT ?author_name  COUNT(?work) AS ?work_nums
    WHERE {
    ?author rdf:type dbo:Writer;
           foaf:name ?author_name;
           dbo:notableWork ?work .
    }
    GROUP BY ?author_name
    ORDER BY DESC(COUNT(?work)) 
    LIMIT 10
    """
    print("get_notablework_num：")
    print(query)
    results = sparql_runner(dbpedia_sparql, query)
    results_processed = result_to_dict(results)
    return results_processed


"""
   电影数据统计部分
"""


def get_movie_nums():
    """
    查询所有电影的数量
    :return: dict {'.1': ['2500']}
    """
    query = """
        PREFIX m: <http://data.linkedmdb.org/resource/movie/>
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        
        SELECT COUNT(?film)
        WHERE {
             ?film rdf:type m:film.
        }
    """
    results = sparql_runner(imdb_sparql, query)
    movie_nums = result_to_dict(results)
    return movie_nums


def get_country_movies():
    """
    # 查询各个国家的电影数量
    :return: dict 国家名以及对应的电影数量
    {'country_name': ['Saudi Arabia', 'Afghanistan', 'India', 'Pakistan', 'Bhutan', 'Mozambique', 'Madagascar', 'Sri Lanka'],
    '.1': ['1', '3', '2341', '118', '1', '1', '1', '34']}
    """
    query_movie_country = """
        PREFIX m:<http://data.linkedmdb.org/resource/movie/>
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

        SELECT ?country_name  COUNT(?film) 
        WHERE {
          ?film rdf:type m:film.
          ?film rdfs:label ?filmTitle.
          ?film m:country ?country.
          ?country m:country_name ?country_name. 
        }
        GROUP BY ?country_name
    
    """
    results = sparql_runner(imdb_sparql, query_movie_country)
    movie_nums = result_to_dict(results)
    return movie_nums


def get_director_movies():
    """
    获取所有的导演及其作品数量
    :return: dict
    """
    query_director_movies = """
    PREFIX m: <http://data.linkedmdb.org/resource/movie/>
    PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        SELECT ?director_name COUNT(?film)
        WHERE {
         ?director rdf:type m:director;
                m:director_name ?director_name.
          ?film m:director ?director.
        }
        GROUP BY ?director_name
    """
    results = sparql_runner(imdb_sparql, query_director_movies)
    return result_to_dict(results)


"""
游戏数据统计部分
"""


def query_game_info():
    """
    查询游戏信息
    ?name 游戏名
    ?designer_name 设计者
    ?date 发行日期
    :return:
    """
    query = """
    SELECT DISTINCT ?name ?designer_name  ?date
         WHERE{
            ?game rdf:type dbo:Game; 
                  foaf:name ?name;
                  dbo:designer ?designer;
                  dbp:date  ?date.
            ?designer foaf:name ?designer_name.
        } 
    """
    results = sparql_runner(dbpedia_sparql, query)
    return show_result_processing(results)


def get_top10_gamecompany():
    """
    出品游戏最多的前十家游戏公司
    :return: dict
    """
    query_vediogame_info = """
         SELECT ?publisher_company COUNT(?video_game)  
         WHERE {
            ?video_game  rdf:type dbo:VideoGame;
                         dbo:publisher ?publisher.
            ?publisher  foaf:name ?publisher_company.
         }
         GROUP BY ?publisher_company
         ORDER BY DESC(COUNT(?video_game) )
         LIMIT 10
    """
    results = sparql_runner(dbpedia_sparql, query_vediogame_info)
    return show_result_processing(results)










