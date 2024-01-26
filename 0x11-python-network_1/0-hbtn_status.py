#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status

- use the package urllib
- You must use a with statement"""

if __name__ == '__main__':
    import urllib.request
    url = 'https://alx-intranet.hbtn.io/status'
    req = urllib.request.Request(url, method='GET')
    with urllib.request.urlopen(req) as response:
        res = response.read()
        # Format and print the response details
        print("Body response:")
        print("\t- type: {}".format(type(res)))
        print("\t- content: {}".format(res))
        print("\t- utf8 content: {}".format(
            res.decode('utf-8')))
