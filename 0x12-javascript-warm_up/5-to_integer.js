#!/usr/bin/node
const processArgv = process.argv;

const firstArg = parseInt(processArgv[2]);

if (!firstArg) console.log('Not a number');
else console.log(`My number: ${firstArg}`);
