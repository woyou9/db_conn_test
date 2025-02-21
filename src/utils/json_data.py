import json


with (open('./data/database_info.json') as database_info_file,
      open('./data/sql_queries.json') as sql_queries_file):
    DATABASE_INFO = json.load(database_info_file)
    SQL_QUERIES = json.load(sql_queries_file).get('random_sql_queries')
