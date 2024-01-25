#!/bin/bash
# sends a POST request from file specified to the passed URL, and displays the body of the response
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
