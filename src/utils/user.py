from src.utils.logger import logger
from src.utils.database_connection import DatabaseConnection


class User:
    def __init__(self, database_connection: DatabaseConnection, username: str, permissions: list, password: str = 'default_pass'):
        self.database_connection = database_connection
        self.username = username
        self.password = password
        self.permissions = permissions
        self.user_status = False
        self.create()
        self.set_permissions(permissions)


    def __str__(self):
        return f'Instance of a test user class.'

    def create(self):
        if self.database_connection.connection:
            logger.info(f'Successfully created user "{self.username}" at "{self.database_connection.host}:{self.database_connection.port}".')
            setattr(self, 'user_status', True)
        else:
            logger.error(f'Could not create user. Connection not established.')
            raise Exception

    def set_permissions(self, permissions: list):
        if self.user_status:
            logger.info(f'Successfully set permissions {permissions} for user "{self.username}".')
        elif not self.user_status:
            logger.info("Can't set permissions for non existing user.")
        else:
            logger.error(f'Could not set permissions. Connection not established.')
            raise Exception

    def delete(self):
        if self.user_status:
            logger.info(f'Successfully deleted user "{self.username}" at "{self.database_connection.host}:{self.database_connection.port}".')
            setattr(self, 'user_status', False)
        elif not self.user_status:
            logger.info("Can't delete non existing user.")
        else:
            logger.error(f'Could not delete user. Connection not established.')
            raise Exception