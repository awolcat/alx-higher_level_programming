#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
        for (let n = 0; n < this.height; n++) {
          for (let m = 0; m < this.height; m++) {
            process.stdout.write(c);
          }
          console.log();
        }
      }
  }
}
module.exports = Square;
