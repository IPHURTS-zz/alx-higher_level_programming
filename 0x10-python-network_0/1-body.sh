#!/bin/bash
# takes in a URL, sends request and displays the body of the response
curl - s "$1" - X GET - L