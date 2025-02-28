import json
from src.utils.logger import logger


try:
    with (open('./data/database_info.json') as database_info_file,
          open('./data/user_data.json') as user_data_file,
          open('./data/sql_queries.json') as sql_queries_file):
        DATABASE_INFO = json.load(database_info_file)
        SQL_QUERIES = json.load(sql_queries_file)
        USER_DATA = json.load(user_data_file)
except FileNotFoundError as e:
    logger.error(f'JSON data file {e.filename} not found or you are attempting to open a wrong file.')
    raise e

