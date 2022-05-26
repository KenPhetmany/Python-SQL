from database import create_db_connection, execute_many_queries, read_query, show_db_query, execute_query

connection = create_db_connection(
    "localhost", "root", "KenPhetmanyDev", "online_movie_rating")

q1 = """
UPDATE reviewers
SET last_name = "Cooper"
WHERE first_name = "Amy"
"""

q2 = """
UPDATE ratings 
SET rating = 5.0
WHERE movie_id = 18 AND reviewer_id = 15;
"""

execute_query(connection, query=q2)
