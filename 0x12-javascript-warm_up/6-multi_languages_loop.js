#!/usr/bin/node

// a script that prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop

const line = ['C is funs', 'Python is cool', 'JavaScript is amazing']

const len = line.length

let num = 0

while (num <= len) {
  console.log(line[num])
  num += 1
}
