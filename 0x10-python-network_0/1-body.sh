#!/bin/bash
# Takes in a URL, sends a request to that URL, and displays the status code of body of the response
curl -sI "$1" | grep 'HTTP/[0-1].[0-2]' | cut -d' ' -f2
