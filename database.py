import sqlite3


DB_PATH = 'our_db_13052024.sqlite3'


with sqlite3.connect(DB_PATH) as connection:
    cursor = connection.cursor()

    # create table
    # query = """
    #       CREATE TABLE IF NOT EXISTS category(
    #            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    #            name VARCHAR(20) NOT NULL,
    #            description TEXT
    #     )
    # """
    # cursor.execute(query)


    # add colum
    # query = """
    #      ALTER TABLE category
    #      ADD COLUMN segment VARCHAR(20)
    # """
    # cursor.execute(query)

    # CREATE DATA
    # query = """
    #     INSTER INTO(name, description, segment)
    #     VALUES ('DELL500', 'old stuff', 'sale')
    # """
    # cursor.execute(query)


