#!/usr/bin/node

const value = process.argv[2];

if (~~value !== 0) {
  console.log(`My number: ${~~value}`);
} else {
  console.log('Not a number');
}
