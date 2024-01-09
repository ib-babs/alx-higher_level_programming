#!/usr/bin/node
const fs = require('fs');
const args = process.argv;
const f1 = fs.readFileSync(args[2], 'utf-8');
const f2 = fs.readFileSync(args[3], 'utf-8');
fs.writeFileSync(args[4], f1 + f2);
