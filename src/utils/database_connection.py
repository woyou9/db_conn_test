import psycopg2
from src.utils.logger import logger


class DatabaseConnection:
    def __init__(self, db_config: dict):
        self.db_name = db_config.get('database_name')
        self.user = db_config.get('user')
        self.password = db_config.get('password')
        self.host = db_config.get('host')
        self.port = db_config.get('port')
        self.connection = None
        self.connect()

    def __str__(self):
        return (f'an instance of DatabaseConnection class, connected to "{self.db_name}" database '
                f'at {self.host}:{self.port} as "{self.user}" user.')

    def connect(self):
        if not all([self.db_name, self.user, self.password, self.host, self.port]):
            logger.error('Database connection details are missing or incomplete.')
            raise ValueError('Incomplete database connection details.')
        try:
            self.connection = psycopg2.connect(
                dbname=self.db_name,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            logger.info(f'Successfully connected to the "{self.db_name}" database. Now using {self.__str__()}')
        except Exception as e:
            logger.error(f'Failed to connect to the "{self.db_name}" database. Exception: {str(e)}')

    def execute_sql(self, sql_query: str, params: tuple = None):
        if not self.connection:
            raise Exception("Database connection not established.")
        try:
            with self.connection.cursor() as cur:
                cur.execute(sql_query, params)
                if cur.description:
                    results = cur.fetchall()
                    if not results:
                        logger.info(f'Query "{sql_query}" with params {params} returned an empty result set.')
                    return results
                self.connection.commit()
                logger.info(f'Query "{sql_query}" with params {params} executed successfully.')
        except Exception as e:
            logger.error(f'Database query failed failed for query: {sql_query} with params: {params}. Exception: {str(e)}')
            self.connection.rollback()

    def close(self):
        if self.connection:
            self.connection.close()
            logger.info(f'Connection to "{self.db_name}" database at {self.host}:{self.port} closed.')
        else:
            logger.error("Can't close non existing connection.")