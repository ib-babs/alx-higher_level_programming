#!/usr/bin/node
const processArgv = require('node:process').argv;
if (processArgv.length < 3) console.log('No argument');
else {
  let i;
  for (i = 2; i < processArgv.length; i++) console.log(processArgv[i]);
}
