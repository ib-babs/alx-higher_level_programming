#!/usr/bin/node
const processArgv = require('node:process').argv;
const firstArg = processArgv[2];
const secondArg = processArgv[3];
console.log(`${firstArg} is ${secondArg}`);
