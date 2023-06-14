#!/usr/bin/node

// Script that print the first argument passed to it

const args = process.argv[2];
console.log(args === undefined ? 'No argument' : args);
