#!/usr/bin/node
const request = require('request');
const parameter = process.argv[2];
// const requestURL = 'http://swapi.co/api/films/';
let numberId = 0;

function myfunction2 (character) {
  if (character.includes('18')) {
    numberId += 1;
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
    console.log(numberId);
  }
});
