#!/usr/bin/python3
"""Filtering Columns of name in the Database Table"""


def filter_states():
    """Filtering columns from states table"""
    if (len(argv) == 4):
        db = MySQLdb.connect(host='localhost', port=3306,
                             user=argv[1], password=argv[2], db=argv[3])
        cur = db.cursor()
        query = """SELECT states.id, states.name FROM states
            WHERE states.name
            LIKE 'N%'
            ORDER BY states.id ASC"""
        cur.execute(query)
        for _ in cur.fetchall():
            print(_)
        cur.close()
        db.close()


if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    filter_states()
