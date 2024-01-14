#!/usr/bin/python3
"""Filtering cities from the database hbtn_0e_4_usa
SQL Injection-free"""


def cities_all():
    """Filter cities columns"""
    if (len(argv) == 5):
        db = MySQLdb.connect(host='localhost', port=3306,
                             user=argv[1], password=argv[2], db=argv[3])
        cur = db.cursor()

        query = """SELECT cities.name FROM cities
            JOIN states
            ON cities.state_id=states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC"""
        cur.execute(query, (argv[4],))
        lists = []

        for rows in cur.fetchall():
            lists.append(' '.join(rows))
        for i in range(len(lists)):
            if (i > 0 and i < len(lists)):
                print(", ", end='')
            print(lists[i], end='')
        print()
        cur.close()
        db.close()


if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    cities_all()
