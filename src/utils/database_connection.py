import psycopg2
from src.utils.logger import logger


class DatabaseConnection:
    def __init__(self, db_config: dict):
        self.dbname = db_config.get('database_name')
        self.user = db_config.get('user')
        self.password = db_config.get('password')
        self.host = db_config.get('host')
        self.port = db_config.get('port')
        self.connection = None
        self.connect()

    def __str__(self):
        return (f'an instance of DatabaseConnection class, connected to "{self.dbname}" database '
                f'at {self.host}:{self.port} as "{self.user}" user.')

    def connect(self):
        if not all([self.dbname, self.user, self.password, self.host, self.port]):
            logger.error('Database connection details are missing or incomplete.')
            raise ValueError('Incomplete database connection details.')
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            logger.info(f'Successfully connected to the "{self.dbname}" database. Now using {self.__str__()}')
        except Exception as e:
            logger.error(f'Failed to connect to the "{self.dbname}" database. Exception: {e.args[1].decode('cp1250')}')

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
            logger.error(f'Database query failed. Exception: {e}')
            self.connection.rollback()

    def close(self):
        if self.connection:
            self.connection.close()
            logger.info(f'Connection to "{self.dbname}" database at {self.host}:{self.port} closed.')
