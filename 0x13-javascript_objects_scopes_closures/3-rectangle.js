#!/usr/bin/node

// Prints a Rectangle with the parameters passed

module.exports = class Rectangle {
  constructor (width, height) {
    if (typeof width === 'number' && typeof height === 'number' && width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }

  print () {
    for (let m = 0; m < this.height; ++m) {
      let m = 0;

      for (; n < this.width; ++n) {
        process.stdout.write('X');
      }

      if (n === this.width) {
        console.log('');
      }
    }
  }
};
