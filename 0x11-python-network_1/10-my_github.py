#!/usr/bin/python3

"""Python script that takes your GitHub credentials
(username and password) and
uses the GitHub API to display your id"""
if __name__ == "__main__":
    import requests
    import sys

    try:
        headers = {"Accept": "application/vnd.github+json",
                   "Authorization": "Bearer {}".format(sys.argv[2])
                   }
        url = "https://api.github.com/users/{}".format(sys.argv[1])
        req = requests.get(url, headers=headers)

        print(req.json().get('id'))
    except ValueError:
        pass
