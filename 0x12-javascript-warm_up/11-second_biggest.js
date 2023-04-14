#!/usr/bin/node

// Convert the arguments to an array
let args = process.argv.slice(2);

// If no argument passed, print 0
if (args.length === 0) {
  console.log(0);
}

// If the number of arguments is 1, print 0
if (args.length === 1) {
  console.log(0);
}

// Convert the arguments to integers
args = args.map(args => parseInt(arg));

// Sort the array of integers
args.sort((a, b) => a - b);

// Print the second biggest integer
console.log(args[args.length - 2]);
