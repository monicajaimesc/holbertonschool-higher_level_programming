#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    // to call its parent's constructor
    // it receives 2 values witdth and hight
    super(size, size);
  }
}

module.exports = Square;
