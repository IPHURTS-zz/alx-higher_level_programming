#!/usr/bin/node
//  all characters in a specific Star Wars movie from the api

const request = require('request');
const movie = process.argv[2];
const url = 'https://swapi.co/api/films/' + movie;

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  let movie = JSON.parse(body);
  for (let character of movie.characters) {
    request(character, function (err, res, body) {
      if (err) {
        console.log(err);
      }
      let chr = JSON.parse(body);
      console.log(chr.name);
    });
  }
});