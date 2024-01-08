#!/usr/bin/node
const processArgv = require('node:process').argv;
function factorial (num) {
  if (!num) {
    num = 1;
    return num;
  }
  return num * factorial(num - 1);
}
const facto = factorial(parseInt(processArgv[2]));
console.log(facto);
