#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body).results;
    const count = results.reduce((count, movie) => {
      if (movie.characters.find((character) => character.endsWith('/18/'))) {
        count += 1;
      }
      return count;
    }, 0);
    console.log(count);
  }
});
