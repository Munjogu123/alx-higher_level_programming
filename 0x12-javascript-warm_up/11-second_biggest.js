#!/usr/bin/node

if (process.argv.length < 3 || process.argv.length === 3) {
  console.log(0);
} else {
  const res = process.argv.sort((a, b) => a - b);
  console.log(res[res.length - 2]);
}
