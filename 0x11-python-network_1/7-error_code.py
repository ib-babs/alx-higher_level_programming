#!/usr/bin/python3

"""Python script that takes in a URL,
sends a request to the URL
and displays the body of the response"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    try:
        req = requests.get(url=url)
        print(req.text)
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(e.code))
