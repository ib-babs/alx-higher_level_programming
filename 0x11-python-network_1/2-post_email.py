#!/usr/bin/python3
"""Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""

if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    req = urllib.request.Request(
        url=url, method='POST',
        data={'email': email},
        headers={"Content-Type: text/plain; charset=utf-8"}
    )
    with urllib.request.urlopen(req) as response:
        print(response.read())
