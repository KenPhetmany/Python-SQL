from database import create_db_connection, execute_many_queries, read_query, show_db_query, execute_query

connection = create_db_connection(
    "localhost", "root", "KenPhetmanyDev", "online_movie_rating")

q1 = """
SELECT * FROM movies
LIMIT 5
"""

q2 = """
SELECT title, collection_in_mil
FROM movies
WHERE collection_in_mil > 300
ORDER BY collection_in_mil DESC
"""

q3 = """
SELECT CONCAT (title, " (", release_year, ")"),
    collection_in_mil
FROM movies 
ORDER BY collection_in_mil DESC
LIMIT 5
"""

q4 = """
SELECT title, AVG(rating) as average_rating
FROM ratings 
INNER JOIN movies 
    ON movies.id = ratings.movie_id
GROUP BY movie_id
ORDER BY average_rating DESC
LIMIT 5
"""

q5 = """
SELECT CONCAT(first_name, " ", last_name), COUNT(*) as num
FROM reviewers
INNER JOIN ratings
ON reviewers.id = ratings.reviewer_id
GROUP BY reviewer_id
ORDER BY num DESC
"""

q6 = """
SELECT *
FROM ratings 
WHERE movie_id = 18 and reviewer_id = 15
"""

read_query(connection, query=q6)
