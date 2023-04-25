#!/usr/bin/node

/*
    script that prints all characters of a Star Wars movie:
    The first argument is the Movie ID 
    Display one character name by line in the same order of the list “characters” in the /films/ endpoint
    You must use the Star wars API
    module request
*/

const request = require('request');
const argv = process.argv[2];
let url = "https://swapi-api.hbtn.io/api/films/" + argv;

request(url, function (err, res, body) {
    if (err) {
        console.log(err);
    }
    let json = JSON.parse(body);
    for (let i = 0; i < json.characters.length; i++) {
        request(json.characters[i], function (err, res, body) {
            if (err) {
                console.log(err);
            }
            let chr = JSON.parse(body);
            console.log(chr.name);
        });
    }
}
);
