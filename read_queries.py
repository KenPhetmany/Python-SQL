from database import create_db_connection, execute_many_queries, read_query, show_db_query, execute_query

connection = create_db_connection(
    "localhost", "root", "KenPhetmanyDev", "online_movie_rating")


q1 = """
SELECT * FROM movies
LIMIT 5
"""

read_query(connection, query=q1)
