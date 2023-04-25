#!/usr/bin/node
// Prints the title of a Star Wars movie where the episode number
// matches the given integer

const request = require('request');
const argv = process.argv[2];
let url = "https://swapi-api.alx-tools.com/api/films/";

request(url + argv, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  let json = JSON.parse(body);
  console.log(json.title);
});