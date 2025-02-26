from datetime import datetime
import pytest
from src.utils.database_connection import DatabaseConnection
from src.utils.json_data import DATABASE_INFO, USER_DATA
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
    db_config: dict = DATABASE_INFO[database_environment]
    db_connection: DatabaseConnection = DatabaseConnection(database_config=db_config)
    yield db_connection
    db_connection.close()


@pytest.fixture
def test_user(database_connection, request):
    role_name: str = request.param
    user: User = User(
                database_connection,
                f'{USER_DATA['user_info'].get('username')}_{datetime.now().strftime("%Y-%m-%d_%H:%M:%S")}',
                USER_DATA['user_roles'].get(role_name),
                USER_DATA['user_info'].get('password'))
    yield user
    user.delete_user()


"""
Analogicznie można zrobić fixture dla każdej roli osobno

@pytest.fixture
def test_user_admin(database_connection):
    user = User(database_connection,
                f'{USER_DATA.get('user_info').get('username')}_{datetime.now().strftime("%Y-%m-%d_%H:%M:%S")}',
                USER_DATA.get('user_roles').get('Admin'),
                USER_DATA.get('user_info').get('password'))
    yield user
    user.delete()


@pytest.fixture
def test_user_pm(database_connection):
    user = User(database_connection,
                f'{USER_DATA.get('user_info').get('username')}_{datetime.now().strftime("%Y-%m-%d_%H:%M:%S")}',
                USER_DATA.get('user_roles').get('PM'),
                USER_DATA.get('user_info').get('password'))
    yield user
    user.delete()


@pytest.fixture
def test_user_worker(database_connection):
    user = User(database_connection,
                f'{USER_DATA.get('user_info').get('username')}_{datetime.now().strftime("%Y-%m-%d_%H:%M:%S")}',
                USER_DATA.get('user_roles').get('Worker'),
                USER_DATA.get('user_info').get('password'))
    yield user
    user.delete()
"""
