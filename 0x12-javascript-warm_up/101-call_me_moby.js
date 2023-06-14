#!/usr/bin/node

// Write a function that executes x times a function

exports.callMeMoby = function (x, theFunction) {
  for (let num = 0; num < x; num++) theFunction()
}
