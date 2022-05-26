from asyncore import read
from database import create_db_connection, execute_many_queries, read_query, show_db_query, execute_query

connection = create_db_connection(
    "localhost", "root", "KenPhetmanyDev", "online_movie_rating")

create_online_movie_rating_db = """
CREATE DATABASE online_movie_rating
"""

create_movies_tables = """
CREATE TABLE movies(
    id INT AUTO_INCREMENT PRIMARY KEY, 
    title VARCHAR(100),
    release_year YEAR(4),
    genre VARCHAR(100),
    collection_in_mil INT
)
"""

create_reviewers_table_query = """
CREATE TABLE reviewers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100)
)
"""

create_ratings_table_query = """
CREATE TABLE ratings (
    movie_id INT,
    reviewer_id INT,
    rating DECIMAL(2,1),
    FOREIGN KEY(movie_id) REFERENCES movies(id),
    FOREIGN KEY(reviewer_id) REFERENCES reviewers(id),
    PRIMARY KEY(movie_id, reviewer_id)
)
"""

alter_table_query = """
ALTER TABLE movies 
MODIFY COLUMN collection_in_mil DECIMAL (4,1)
"""

drop_table_query = """
DROP TABLE ratings
"""
