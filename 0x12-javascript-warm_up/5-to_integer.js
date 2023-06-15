#!/usr/bin/node

//a script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer

const nums = Math.floor(Number(process.argv[2]));

console.log(isNaN(nums) ? 'Not a number' : `My number: ${nums}`); 
