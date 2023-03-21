#!/usr/bin/python3
<<<<<<< HEAD

"""
    A script that lists all cities in a state from the database hbtn_0e_0_usa
    Username, password and database name and state are given as user args
"""


import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)

    cursor = db.cursor()

    sql = """SELECT cities.name
          FROM states
          INNER JOIN cities ON states.id = cities.state_id
          WHERE states.name = %s
          ORDER BY cities.id ASC"""

    cursor.execute(sql, (sys.argv[4],))

    data = cursor.fetchall()

    print(", ".join([city[0] for city in data]))

    cursor.close()
    db.close()
=======
"""
lists all cities from the database
"""
if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    cont = 0
    conect = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                             passwd=argv[2], db=argv[3], charset="utf8")
    cursor = conect.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name
    FROM cities
    LEFT JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC""")
    query_rows = cursor.fetchall()
    for row in query_rows:
        if row[2] == argv[4]:
            if cont > 0:
                print(", ", end="")
            print(row[1], end="")
            cont = cont + 1
    print()
    cursor.close()
    conect.close()
>>>>>>> b95bb6843f82300f1bcc5e44f6aff07f0f6e7031
