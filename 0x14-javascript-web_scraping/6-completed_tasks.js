#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (!error) {
    const contents = JSON.parse(body);
    const completed = {};
    contents.forEach((content) => {
      if (content.completed && completed[content.userId] === undefined) {
        completed[userId] = 1;
      } else if (content.completed) {
        completed[content.userId] += 1;
      }
    });
    console.log(completed);
  }
});
