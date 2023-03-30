#!/bin/bash
# takes in a URL, sends a request, and displays the size  response
curl - sI "$1" | grep 'Content-Length' | awk '{print $2}'
