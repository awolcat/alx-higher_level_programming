#!/usr/bin/node

const ogSquare = require('./5-square.js');

class Square extends ogSquare {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
        for (let n = 0; n < this.size; n++) {
          for (let m = 0; m < this.size; m++) {
            process.stdout.write(c);
          }
          console.log();
        }
      }
  }
}
module.exports = Square;
