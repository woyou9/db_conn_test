from src.utils.database_connection import DatabaseConnection
from src.utils.json_data import SQL_QUERIES


def test_01(localhost_connection: DatabaseConnection) -> None:

    rows = localhost_connection.execute_sql(SQL_QUERIES.get('select_customers'))
    for row in rows:
        print(row)
    print('')

    rows = localhost_connection.execute_sql(SQL_QUERIES.get('select_orders'))
    for row in rows:
        print(row)
    print('')

    rows = localhost_connection.execute_sql(SQL_QUERIES.get('select_products'))
    for row in rows:
        print(row)
    print('')
