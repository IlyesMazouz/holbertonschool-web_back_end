#!/usr/bin/env python3

"""
A module for providing functions to handle
logging and database connections securely
"""

import logging
import os
import mysql.connector


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Get a connector to the MySQL database using environment variables
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


def main():
    """
    Connect to the database, retrieve all rows from the users table,
    and log each row with filtered format
    """
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("user_data")

    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM users;")
    rows = cursor.fetchall()

    for row in rows:
        filtered_row = "; ".join([f"{field}=***" for field in row])
        logger.info(filtered_row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
