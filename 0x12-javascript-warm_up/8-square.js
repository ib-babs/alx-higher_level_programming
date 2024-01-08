#!/usr/bin/node
const processArgv = process.argv;

const firstArg = parseInt(processArgv[2]);

if (!firstArg) console.log('Missing size');
else {
  let i;
  for (i = 0; i < firstArg; i++) console.log('X'.repeat(firstArg));
}
