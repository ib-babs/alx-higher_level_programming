#!/usr/bin/python3
"""
Python script that takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

if __name__ == "__main__":
    import requests
    import sys
    letter = ""
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    # URL
    post_url = "http://0.0.0.0:5000/search_user"

    req = requests.post(post_url, data={"q": letter})
    try:
        # Convert output to json
        json_req = req.json()

        # Check if json_req variable exist and non-empty
        if json_req != {}:
            print("[{}] {}".format(json_req.get('id'),
                                   json_req.get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
