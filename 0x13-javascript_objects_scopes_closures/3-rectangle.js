#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    // positive integer >
    if (w > 0 && h > 0) {
      // public properties
      this.width = w;
      this.height = h;
    }
  }

  // public methods
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
