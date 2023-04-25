#!/usr/bin/node
/*
script that computes the number of tasks completed by user id.

The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
Only print users with completed task
 use the module request
*/

const request = require('request');
const url = process.argv[2];    
let json = {};
let count = 0;
let users = {};

request(url, function (err, res, body) {
    if (err) {
        console.log(err);
    }
    json = JSON.parse(body);
    for (let i = 0; i < json.length; i++) {
        if (json[i].completed === true) {
            if (users[json[i].userId] === undefined) {
                users[json[i].userId] = 1;
            } else {
                users[json[i].userId] += 1;
            }
        }
    }
    console.log(users);
    }
);