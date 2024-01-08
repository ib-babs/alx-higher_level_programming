#!/usr/bin/node
const processArgv = process.argv;

const firstArg = parseInt(processArgv[2]);

if (!firstArg) console.log('Missing number of occurrences');
else {
  let i;
  for (i = 0; i < firstArg; i++) {
    console.log('C is fun');
  }
}
