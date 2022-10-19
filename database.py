
import sqlite3

conn = sqlite3.connect("database.sqlite")

cursor = conn.cursor()

# sql_query = """ CREATE TABLE database (
#     id INTEGER PRIMARY KEY,
#     reviews TEXT NOT NULL,
#     sentiment INTEGER NOT NULL
# )"""

sql_query = """ CREATE TABLE reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    reviews TEXT NOT NULL
)"""


sql_query_two = """ CREATE TABLE sentiments (
    id_sentiment INTEGER PRIMARY KEY AUTOINCREMENT,
    positive NUMERIC NOT NULL,
    negative NUMERIC NOT NULL,
    id__sentiment_review INTEGER,
    FOREIGN KEY(id__sentiment_review) REFERENCES reviews(id)
)"""

cursor.execute(sql_query)
cursor.execute(sql_query_two)
rows = cursor.fetchall()