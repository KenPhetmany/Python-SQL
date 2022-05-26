from mysql.connector import connect, Error


def create_db_connection(host_name, user_name, user_password, db):
    connection = None
    try:
        connection = connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db
        )
        print("MySQL Database connection successful \n")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"Error: '{e}'")


def show_db_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        for db in cursor:
            print(db)
    except Error as e:
        print(f"Error: '{e}'")
