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
        url=url,
        data={"email": email},
        method='POST',
    )
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
