#!/usr/bin/node

const num = process.argv[2];

if (~~num !== 0) {
  for (let i = 0; i < ~~num; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
