#!/usr/bin/node

// Script that print the first argument passed to it

const args = process.argv.slice(2);
const oneArgument = args[0] === 'undefined' ? 'No argument' : process.argv[1];
console.log(oneArgument);
