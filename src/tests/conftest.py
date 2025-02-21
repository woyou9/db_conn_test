import pytest
from src.utils.database_connection import DatabaseConnection
from src.utils.json_data import DATABASE_INFO


@pytest.fixture
def localhost_connection():
    db_connection: DatabaseConnection = DatabaseConnection(DATABASE_INFO['localhost_connection'].get('database_name'),
                                                           DATABASE_INFO['localhost_connection'].get('user'),
                                                           DATABASE_INFO['localhost_connection'].get('password'),
                                                           DATABASE_INFO['localhost_connection'].get('host'),
                                                           DATABASE_INFO['localhost_connection'].get('port'))
    yield db_connection
    db_connection.close()
