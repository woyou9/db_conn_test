from src.utils.logger import logger
from src.utils.database_connection import DatabaseConnection


class User:
    def __init__(self, database_connection: DatabaseConnection, username: str, permissions: list, password: str = 'default_pass'):
        self.database_connection = database_connection
        self.username = username
        self.password = password
        self.permissions = permissions
        self.user_status = False
        self.create_user()
        self.set_permissions(permissions)

    def __str__(self):
        return f'Test user with username {self.username} and permissions: {self.permissions}.'

    def create_user(self):
        if not self.database_connection.connection:
            logger.error('Could not create user. Connection not established.')
            raise Exception('Database connection not established.')
        else:
            # sql tworzący usera
            logger.info(f'Successfully created user "{self.username}" at "{self.database_connection.host}:{self.database_connection.port}".')
            self.user_status = True

    def set_permissions(self, permissions: list):
        if not self.database_connection.connection:
            logger.error('Could not set permissions. Connection not established.')
            raise Exception('Database connection not established.')
        if not self.user_status:
            logger.error("Can't set permissions for non existing user.")
            raise Exception("Can't set permissions - user doesn't exist.")
        # sql nadający uprawnienia userowi
        logger.info(f'Successfully set permissions {permissions} for user "{self.username}".')

    def delete_user(self):
        if not self.database_connection.connection:
            logger.error(f'Could not delete user. Connection not established.')
            raise Exception('Database connection not established.')
        if not self.user_status:
            logger.error("Can't delete non existing user.")
            raise Exception("Can't delete non existing user.")
        # sql usuwający usera
        logger.info(f'Successfully deleted user "{self.username}" at "{self.database_connection.host}:{self.database_connection.port}".')
        self.user_status = False