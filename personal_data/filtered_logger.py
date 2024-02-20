#!/usr/bin/env python3

"""
filtered_logger.py: A module for providing functions
to handle logging and database connections securely
"""

import logging
import mysql.connector
import os


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    get a connector to the MySQL database using environment variables
    """
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    database = os.getenv("PERSONAL_DATA_DB_NAME")

    try:
        db = mysql.connector.connect(
            host=host, user=username, password=password, database=database
        )
        return db
    except mysql.connector.Error as err:
        print("Error connecting to MySQL database:", err)


if __name__ == "__main__":
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM users;")
    for row in cursor:
        print(row[0])
    cursor.close()
    db.close()
