from database import create_database, create_db_connection, show_db_query

connection = create_db_connection(
    "localhost", "root", "KenPhetmanyDev", "school")

q1 = """
CREATE DATABASE online_movie_rating
"""

q2 = """
SHOW DATABASES
"""

show_db_query(connection, query=q2)
