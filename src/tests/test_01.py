import random
from src.utils.database_connection import DatabaseConnection
from src.utils.json_data import SQL_QUERIES
from src.utils.user import User


RANDOM_SQL_QUERIES = SQL_QUERIES.get('random_sql_queries')
RANDOM_SQL_QUERIES_WITH_PARAMS = SQL_QUERIES.get('random_sql_queries_with_params')
RANDOM_SQL_INSERTS = SQL_QUERIES.get('random_sql_inserts')
RANDOM_SQL_DELETES = SQL_QUERIES.get('random_sql_deletes')


def test_selects(database_connection: DatabaseConnection, test_user_admin: User) -> None:
    rows: list[tuple] = database_connection.execute_sql(RANDOM_SQL_QUERIES.get('select_customers'))

    print('')
    for row in rows:
        print(row)
    print('')

    rows: list[tuple] = database_connection.execute_sql(RANDOM_SQL_QUERIES.get('select_orders'))
    print('')
    for row in rows:
        print(row)
    print('')

    rows: list[tuple] = database_connection.execute_sql(RANDOM_SQL_QUERIES.get('select_products'))
    print('')
    for row in rows:
        print(row)
    print('')


def test_selects_with_params(database_connection: DatabaseConnection, test_user_worker: User) -> None:
    rows: list[tuple] = database_connection.execute_sql(RANDOM_SQL_QUERIES_WITH_PARAMS.get('select_order_by_customer_id'),
                                                         ('HANAR',))
    print('')
    for row in rows:
        print(row)
    print('')

    assert len(rows) == 14
    for row in rows:
        assert 'HANAR' in row

    rows: list[tuple] = database_connection.execute_sql(RANDOM_SQL_QUERIES_WITH_PARAMS.get('select_customer_by_country_and_city'),
                                                         ('UK', 'London'))
    print('')
    for row in rows:
        print(row)
    print('')

    assert len(rows) == 6
    for row in rows:
        assert 'UK' in row and 'London' in row


def test_insert_and_delete(database_connection: DatabaseConnection, test_user_pm: User) -> None:
    customer_id = random.randrange(10, 100)

    database_connection.execute_sql(RANDOM_SQL_INSERTS.get('insert_into_categories_with_id'),
                                     (customer_id,))
    rows: list[tuple] = database_connection.execute_sql(f"SELECT * FROM categories WHERE category_id = %s",
                                                         (customer_id,))

    assert (customer_id, 'Ass', 'It is just so ass', None) in rows

    database_connection.execute_sql(RANDOM_SQL_DELETES.get('delete_from_categories_by_id'),
                                     (customer_id,))

    rows: list[tuple] = database_connection.execute_sql(f"SELECT * FROM categories WHERE category_id = %s",
                                                         (customer_id,))
    assert rows == []
