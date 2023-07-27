#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const completed_task = {};
  body.forEach((to_do) => {
    if (to_do.completed) {
      if (!completed_task[to_do.userId]) {
        completedtask[to_do.userId] = 1;
      } else {
        completed_task[to_do.userId] += 1;
      }
    }
  });
  console.log(completed_task);
});
