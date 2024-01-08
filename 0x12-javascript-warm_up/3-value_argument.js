#!/usr/bin/node
const processArgv = process.argv;
let recordLength;
for (recordLength = 0; processArgv[recordLength]; recordLength++);

if (recordLength < 3) console.log('No argument');
else {
  let i;
  for (i = 2; i < recordLength; i++) console.log(processArgv[i]);
}
