#!/usr/bin/node

// a script that prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop

const line = ['C is funs', 'Python is cool', 'JavaScript is amazing'];

const len = line.length;

for (let n = 0; n < len; n++) { 
   console.log(line[n]);
}
