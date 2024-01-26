#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status

- use the package urllib
- You must use a with statement"""

if __name__ == '__main__':
    import urllib.request
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        res = response.read()
        result = """Body response:
    - type: {}
    - content: {}
    - utf8 content: {}""".format(type(res), res, response.msg)
        print(result)
