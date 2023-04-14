#!/usr/bin/node

//script that print a message depending of the number of arguments passed

const number = process.argv.length;

if (number === 2) {
	console.log('No argument');
}
else if (number === 3) {
	console.log('Argument found');
} else {
	console.log('Argument found');
}
