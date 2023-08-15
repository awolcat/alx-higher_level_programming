#!/usr/bin/node

exports.esrever = function (list) {
  const newArr = [];
  let m = 0;
  for (let n = list.length - 1; n > -1; n--) {
    newArr[m] = list[n];
    m++;
  }
  return newArr;
};
