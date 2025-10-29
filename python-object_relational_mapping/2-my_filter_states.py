#!/usr/bin/python3
"""Module"""
import MySQLdb
import sys


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
        )
        cursor = db.cursor()
        query = (
            "SELECT * FROM states "
            "WHERE name = '{}' "
            "ORDER BY id ASC".format(state_name_searched)
        )
        cursor.execute(query)
        states = cursor.fetchall()

        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        if 'db' in locals() and db:
            db.close()