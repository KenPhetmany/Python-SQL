from mysql.connector import connect, Error


def create_db_connection(host_name, user_name, user_password, db):
    try:
        with connect(
            host=host_name,
            user=user_name,
            password=user_password
        ) as connection:
            print(f"Success: '{connection}'")
    except Error as e:
        print(e)

    return connection


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"Error: '{e}'")
