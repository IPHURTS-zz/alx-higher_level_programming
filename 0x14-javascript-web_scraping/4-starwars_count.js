#!/usr/bin/node

/*
 script that prints the number of movies where the character “Wedge Antilles” is present.

The first argument is: https://swapi-api.alx-tools.com/api/films/
Wedge Antilles is character ID 18 
 use the module request
*/

const request = require('request');
const argv = process.argv[2];
let url = "https://swapi-api.alx.io/api/films/";
let count = 0;

request(url, function (err, res, body) {
    if (err) {
        console.log(err);
    }
    let json = JSON.parse(body);
    for (let i = 0; i < json.results.length; i++) {
        for (let j = 0; j < json.results[i].characters.length; j++) {
        if (json.results[i].characters[j].includes("18")) {
            count++;
        }
        }
    }
    console.log(count);
    }
);

