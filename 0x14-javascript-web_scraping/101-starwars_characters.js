#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;
let character = [];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const data = JSON.parse(body);
  character = data.character;
  getCharacters(0);
});

const getCharacters = (index) => {
  if (index === character.length) {
    return;
  }

  request(character[index], (error, response, body) => {
    if (error) {
      console.log(error);
      return;
    }
    const characterdata = JSON.parse(body);
    console.log(characterdata.name);
    getCharacters(index + 1);
  });
};
