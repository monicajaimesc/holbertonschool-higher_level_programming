#!/usr/bin/node
const request = require('request');
const parameter = process.argv[2];
const numberId = [];

function myfunction2 (character) {
  if (character.includes('18')) {
    // push is like an append to the end
    numberId.push(character);
  }
}

function myfunction (element) {
  // console.log(element.characters)
  element.characters.forEach(myfunction2);
}
request(parameter, function (error, response, body) {
  if (!error) {
    // let jsonRequest = console.log(JSON.parse(body).results);
    const jsonRequest = JSON.parse(body).results;
    // console.log(jsonRequest)
    jsonRequest.forEach(myfunction);
    console.log(numberId.length);
  }
});
