import pytest
from src.utils.database_connection import DatabaseConnection
from src.utils.json_data import DATABASE_INFO
from src.utils.user import User


def pytest_addoption(parser):
    parser.addoption(
        '--env',
        action='store',
        default='localhost',
        choices=['localhost', 'preprod', 'test'],
        help='Choose the environment to run tests in.'
    )


@pytest.fixture
def database_environment(request):
    return request.config.getoption('--env')


@pytest.fixture
def database_connection(database_environment):
    db_config = DATABASE_INFO[database_environment]
    db_connection: DatabaseConnection = DatabaseConnection(db_config.get('database_name'),
                                                           db_config.get('user'),
                                                           db_config.get('password'),
                                                           db_config.get('host'),
                                                           db_config.get('port'))
    yield db_connection
    db_connection.close()


@pytest.fixture
def test_user(database_connection):
    test_permissions = ['add', 'edit', 'delete', 'almighty']
    user = User(database_connection, username='test_user')
    user.create()
    user.set_permissions(test_permissions)
    # usunąć create/set_permissions i obsłużyć to przy tworzeniu instancji?
    yield user
    user.delete()
