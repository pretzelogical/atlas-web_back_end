#!/usr/bin/env node
const express = require('express');
const app = express();
const fs = require('fs').promises;
const port = 1245;

async function countStudents(path) {
  try {
    await fs.access(path, fs.constants.R_OK | fs.constants.F_OK);
  } catch (e) {
    throw new Error('Cannot load the database');
  }
  const database = ((await fs.readFile(path)).toString().split('\n'))
    .filter((elem) => elem.trim() !== '');
  const fields = { CS: [], SWE: [] };

  for (let i = 1; i < database.length; i++) {
    const entry = database[i].split(',');
    if (entry[entry.length - 1] in fields) {
      fields[entry[entry.length - 1]].push(entry[0]);
    }
  }
  const studentsCS = fields.CS.join(', ');
  const studentsSWE = fields.SWE.join(', ');
  return [
    'This is the list of our students',
    `Number of students: ${database.length - 1}`,
    `Number of students in CS: ${fields.CS.length}. List: ${studentsCS}`,
    `Number of students in SWE: ${fields.SWE.length}. List: ${studentsSWE}`
  ];
}

app.get('/', (req, res) => {
  res.set('Content-Type', 'text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  res.set('Content-Type', 'text/plain');
  res.send((await countStudents(process.argv[2])).join('\n'));
});
app.listen(port);

module.exports = app;

