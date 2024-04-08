#!/usr/bin/node

const num = process.argv[2];

if (~~num !== 0) {
  for (let i = 0; i < ~~num; i++) {
    console.log('X'.repeat(~~num));
  }
} else {
  console.log('Missing size');
}
