#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
let count = 0;
request(url, (err, response, body) => {
  if (err) throw err;
  const films = JSON.parse(body).results;
  for (const obj of films) {
    for (const characters of obj.characters) {
      const charactersList = characters.split('/');
      if (charactersList[charactersList.length - 2] === '18') {
        count = count + 1;
      }
    }
  }
  console.log(count);
});
