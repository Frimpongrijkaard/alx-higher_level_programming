#!/usr/bin/node

// Script that print the first argument passed to it

const args = process.argv.length
console.log(args === 2 ? 'No argument' : args === 3 ? 'Argument found' : 'Arguments found')
