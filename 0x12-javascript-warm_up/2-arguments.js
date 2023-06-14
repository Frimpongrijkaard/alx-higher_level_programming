#!/usr/bin/node

//script that print a message depending of the number of arguments passed

const args = process.argv.slice(2);

if (args.length === 0) { console.log('NO argument')
} else if (args.length === 1) { console.log('Argument found')
} else {
    console.log('Argument found')
}
