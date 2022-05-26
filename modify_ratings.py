from database import create_db_connection, execute_many_queries, execute_modify_rating, read_query, show_db_query, execute_query

connection = create_db_connection(
    "localhost", "root", "KenPhetmanyDev", "online_movie_rating")


movie_id = input("Enter movie id: ")
reviewer_id = input("Enter reviewer id: ")
new_rating = input("Enter new rating: ")
update_query = """
UPDATE
    ratings
SET
    rating = %s
WHERE
    movie_id = %s AND reviewer_id = %s;

SELECT *
FROM ratings
WHERE
    movie_id = %s AND reviewer_id = %s
"""
val_tuple = (
    new_rating,
    movie_id,
    reviewer_id,
    movie_id,
    reviewer_id,
)

execute_modify_rating(connection, query=update_query, val_tuple=val_tuple)
