#!/usr/bin/python3
"""Passing arg as column value with command line
Vulnerable to SQL Injection"""


def my_filter_states():
    """Passing arg to the table improperly"""
    if (len(argv) == 5):
        db = MySQLdb.connect(host='localhost', port=3306,
                             user=argv[1], password=argv[2], db=argv[3])
        cur = db.cursor()
        query = """SELECT * FROM states
            WHERE states.name='{}'
            ORDER BY states.id ASC""".format(
            argv[4])
        cur.execute(query)
        for _ in cur.fetchall():
            print(_)
        cur.close()
        db.close()


if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    my_filter_states()
