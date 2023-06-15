#!/usr/bin/node

//a script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer

const nums = Maths.floor(number(process.argv[2]));

console.log(number.isInteger(nums) ? `My number: ${nums}`: 'Not a number'); 
