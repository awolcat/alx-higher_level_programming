#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const obj = {};
let completed = 0;

request(url, (error, response, body) => {
  if (error) throw error;
  const tasks = JSON.parse(body);
  for (let i = 1; i < 11; i++) {
    for (const task of tasks) {
      if (task.userId === i && task.completed) completed++;
    }
    if (completed > 0) {
      obj[i] = completed;
      completed = 0;
    }
  }
  console.log(obj);
});
