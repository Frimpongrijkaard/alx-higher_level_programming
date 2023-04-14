#!/usr/bin/node

//a script that prints a square

const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
  console.log('Missing size');
} else {

  for (let row = 0; row < size; row++) {

    let square = '';

    for (let col = 0; col < size; col++)
	    square += 'X';
    console.log(square);
  }
}
