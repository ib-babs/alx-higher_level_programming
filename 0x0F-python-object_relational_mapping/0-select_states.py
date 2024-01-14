#!/usr/bin/python3
"""Starting Connection in MySQL"""


def select_states():
    """Initiate connection and start selection"""
    if (len(argv) == 4):
        db = MySQLdb.connect(host='localhost', port=3306,
                             user=argv[1], password=argv[2], db=argv[3])
        cur = db.cursor()
        cur.execute("SELECT * FROM states ORDER BY states.id ASC")
        for _ in cur.fetchall():
            print(_)
        cur.close()
        db.close()


if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    select_states()
