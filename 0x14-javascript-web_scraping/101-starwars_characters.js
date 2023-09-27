#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (error, response, body) => {
  if (error) throw error;
  const film = JSON.parse(body);
  const characters = film.characters;

  for (const character of characters) {
    request(character, (error, response, body) => {
      if (error) throw error;
      const charName = JSON.parse(body).name;
      console.log(charName);
    });
  }
});
