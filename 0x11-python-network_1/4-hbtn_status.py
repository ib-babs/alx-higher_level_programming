#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status
using `requests` package"""
if __name__ == "__main__":
    import requests
    url = "https://alx-intranet.hbtn.io/status"
    req = requests.get(url)
    content = req.content.decode('utf-8')
    res = """Body response:
    - type: {}
    - content: {}""".format(type(content), content)
    print(res)
