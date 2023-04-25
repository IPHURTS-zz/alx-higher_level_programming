#!/usr/bin/node

/*
script that display the status code of a GET request.
The first argument is the URL to request (GET)
The status code must be printed like this: code: <status code>
You must use the module request
*/

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
    if (error) {
        console.log(error);
    } else {
        console.log('code: ' + response.statusCode);
    }
    }
);


