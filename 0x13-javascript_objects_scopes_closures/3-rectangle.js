#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    // positive integer >
    if (w > 0 && h > 0) {
      // public properties
      this.width = w;
      this.height = h;
      // public methods
      this.print = function () {
        for (let i = 0; i < h; i++) {
          console.log('X'.repeat(w));
        }
      }
    }
  }
}

module.exports = Rectangle;
