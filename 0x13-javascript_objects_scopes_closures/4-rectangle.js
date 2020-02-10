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

  // instance method that exchanges the widht and the height
  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
