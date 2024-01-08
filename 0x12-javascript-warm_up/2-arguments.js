#!/usr/bin/node
const processArgv = require('node:process').argv;
if (processArgv.length < 3) console.log('No argument');
else console.log('Argument found');
