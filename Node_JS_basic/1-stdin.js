#!/usr/bin/env node
process.stdout.write('Welcome to Holberton School, what is your name?\n');

process.stdin.on('data', (data) => {
  const input = data.toString();
  process.stdout.write(`Your name is: ${input}`);
});

process.on('exit', (code) => {
  process.stdout.write('This important software is now closing\n');
});
