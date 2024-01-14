#!/usr/bin/python3
"""Passing arg as column value with command line
Invulnerable to SQL Injection"""


def my_safe_filter_states():
    """Safe filtering"""
    if (len(argv) == 5):
        db = MySQLdb.connect(host='localhost', port=3306,
                             user=argv[1], password=argv[2], db=argv[3])
        cur = db.cursor()

        query = """SELECT * FROM states
            WHERE states.name = %s
            ORDER BY states.id ASC"""
        cur.execute(query, (argv[4], ))
        for _ in cur.fetchall():
            print(_)
        cur.close()
        db.close()


if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    my_safe_filter_states()
