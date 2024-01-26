#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status

- use the package urllib
- You must use a with statement"""
import urllib.request

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        res = response.read()
        result = """Body response:
    - type: {}
    - content: {}
    - utf content: {}""".format(type(res), res, response.msg)
        print(result)
