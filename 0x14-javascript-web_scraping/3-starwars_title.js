#!/usr/bin/node

/*
script that prints the number of movies where the character “Wedge Antilles” is present.

The first argument is the API URL of the Star wars API: https://swapi-api.alx-tools.com/api/films/
Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
You must use the module request
 */

const request = require('request');
const url = "https://swapi-api.alx-tools.com/api/films/;";
const wedge = "https://swapi-api.alx-tools.com/api/people/18/";

request(url, function (error, response, body) {
    if (error) {
        console.log(error);
    } else {
        let count = 0;
        const films = JSON.parse(body).results;
        for (const film of films) {
            for (const character of film.characters) {
                if (character === wedge) {
                    count++;
                }
            }
        }
        console.log(count);
    }
}
);

