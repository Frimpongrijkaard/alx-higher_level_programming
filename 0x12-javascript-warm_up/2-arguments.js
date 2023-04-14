#!/usr/bin/node

//script that print a message depending of the number of arguments passed

const number = process.argv.length;
console.log(number === 2 ? 'No argument' : number === 3 ? 'Argument found' : 'Arguments found');
