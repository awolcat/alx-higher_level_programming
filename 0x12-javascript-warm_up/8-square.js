#!/usr/bin/node

const args = process.argv;
const arg = args[2];
const number = parseInt(arg);
if (Object.is(NaN, number)) {
  console.log('Missing size');
} else {
  let c = '';
  for (let idx = 0; idx < number; idx++) {
    c += 'X';
  }
  for (let idx = 0; idx < number; idx++) {
    console.log(c);
  }
}
