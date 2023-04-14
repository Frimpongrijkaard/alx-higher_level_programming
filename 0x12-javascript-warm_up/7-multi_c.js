 #!/usr/bin/node 

// a script that prints x times “C is fun”
const x = Math.floor(Number(process.argv[2]));

if (isNaN(x)) {

  console.log('Missing number of occurrences');

} else {
  for (let num = 0; num < x; num++) {

    console.log('C is fun');
  }
}
