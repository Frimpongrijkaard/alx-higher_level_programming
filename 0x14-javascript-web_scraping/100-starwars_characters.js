#!/usr/bin/node

const request = require('request');

const movie_Id = process.argv[2];
const url = `https://swapi.dev/api/films/${movie_Id}/`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const data = JSON.parse(body);
  const characters = data.characters;
  for (const character of characters) {
    request(character, (error, response, body) => {
      if (error) {
        console.log(error);
        return;
      }
      const characterdata = JSON.parse(body);
      console.log(characterdata.name);
    });
  }
});
