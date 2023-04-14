#!/usr/bin/node

//Script that print the first argument passed to it

const args = process.argv[2]

if (typeof args === 'undefined') {
	console.log('No argument');
} else {
	console.log(args);
}
