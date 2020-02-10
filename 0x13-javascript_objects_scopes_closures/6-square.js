#!/usr/bin/node
const Square = require('./5-square');
Square.prototype.charPrint = function (c) {
  if (c === undefined) {
    c = 'X';
  }
  let index = 0;
  while (index < this.width) {
    index++;
    // for (let index = 0; index < this.width; index++) {
    console.log(c.repeat(this.height));
  }
};

module.exports = Square;
