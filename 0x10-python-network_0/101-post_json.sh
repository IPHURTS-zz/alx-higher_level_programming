#!/bin/bash
# a Bash script  containing You got me!, in the body of the response.
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"