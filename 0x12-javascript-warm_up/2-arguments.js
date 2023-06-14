#!/usr/bin/node

//script that print a message depending of the number of arguments passed

const args = process.argv;
if (args.length === 2)
{
	console.log("NO argument");
}
else if (args.length === 3)
{
	console.log("Argument found");
}
else
{
	console.log("Argument found");
}
