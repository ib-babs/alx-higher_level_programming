#!/usr/bin/python3
"""Python script that takes in a URL,
sends a request to the URL
and displays the body of the response (decoded in utf-8)."""

if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    req = urllib.request.Request(url=url)

    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
