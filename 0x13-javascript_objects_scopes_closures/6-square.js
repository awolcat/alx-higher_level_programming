#!/usr/bin/node

const ogSquare = require('./5-square.js');

class Square extends ogSquare {
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
