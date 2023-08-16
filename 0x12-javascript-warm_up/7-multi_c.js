#!/usr/bin/node

const args = process.argv;
const arg = args[2];
const number = parseInt(arg);
if (Object.is(NaN, number)) {
  console.log('Missing number of occurrences');
} else {
  for (let idx = 0; idx < number; idx++) {
    console.log('C is fun');
  }
}
