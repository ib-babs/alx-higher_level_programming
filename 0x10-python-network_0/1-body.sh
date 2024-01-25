#!/bin/bash
# Takes in a URL, sends a request to that URL, and displays the body of the response if 
# status code is 200
statusCode=$(curl -sI "$1" | grep 'HTTP/[0-1].[0-9]' | cut -d' ' -f2)

if [ "$statusCode" -eq 200 ]; then
    curl -s "$1"
fi
