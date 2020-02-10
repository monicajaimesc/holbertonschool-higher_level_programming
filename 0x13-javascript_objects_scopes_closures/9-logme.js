#!/usr/bin/node
let counter = 0;
exports.logMe = function (item) {
  // `${counter}: ${item}`
  console.log(counter + ': ' + item);
  counter++;
};
