#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/people/18';
request(url, (err, response, body) => {
  if (err) throw err;
  const films = JSON.parse(body).films;
  console.log(films.length);
});
