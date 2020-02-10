#!/usr/bin/node
// constructor will take two arguments
class Rectangle {
  constructor (w, h) {
    // positive integer >
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
