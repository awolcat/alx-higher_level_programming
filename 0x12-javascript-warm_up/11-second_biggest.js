#!/usr/bin/node

// Collect array
const array = process.argv;
array.shift();
array.shift();

// Parse members to integers
const arr = [];
for (let i = 0; i < array.length; i++) {
  arr[i] = parseInt(array[i]);
}

if (arr.length <= 1) {
  console.log(0);
} else {
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length - 1; j++) {
      if (arr[j] < arr[j + 1]) {
        const temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
  console.log(arr[1]);
}
