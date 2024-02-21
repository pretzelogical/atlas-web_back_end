#!/usr/bin/env node
const fs = require('fs');

function countStudents(path) {
  if (!fs.existsSync(path)) {
    throw new Error('Cannot load the database');
  }

  const databaseBytes = fs.readFileSync(path);
  const database = (databaseBytes.toString().split('\n'))
    .filter((elem) => elem.trim() !== '');
  const fields = { CS: [], SWE: [] };

  console.log(`Number of students: ${database.length - 1}`);
  for (let i = 1; i < database.length; i += 1) {
    const entry = database[i].split(',');
    if (entry[entry.length - 1] in fields) {
      fields[entry[entry.length - 1]].push(entry[0]);
    }
  }
  const csStudents = fields.CS.join(', ');
  const sweStudents = fields.SWE.join(', ');
  console.log(
    `Number of students in CS: ${fields.CS.length}. List: ${csStudents}`,
  );
  console.log(
    `Number of students in SWE: ${fields.SWE.length}. List: ${sweStudents}`,
  );
}

module.exports = countStudents;
