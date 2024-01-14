#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""


def cities_all():
    """Getting all cities columns"""
    if (len(argv) == 4):
        db = MySQLdb.connect(host='localhost', port=3306,
                             user=argv[1], password=argv[2], db=argv[3])
        cur = db.cursor()

        query = """SELECT cities.id, cities.name, states.name FROM cities
            JOIN states
            ON cities.state_id=states.id
            ORDER BY cities.id ASC"""
        cur.execute(query)
        for _ in cur.fetchall():
            print(_)
        cur.close()
        db.close()


if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    cities_all()
