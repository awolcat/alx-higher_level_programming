#!/usr/bin/node

const args = process.argv;
const number = parseInt(args[2]);
function factorial (num) {
  if (num === 1 || Object.is(NaN, num)) {
    return 1;
  }
  return num * factorial(num - 1);
}
console.log(factorial(number));
