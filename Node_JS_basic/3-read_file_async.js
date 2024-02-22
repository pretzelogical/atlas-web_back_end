#!/usr/bin/env node
const fs = require('fs').promises;

async function countStudents(path) {
  try {
    await fs.access(path, fs.constants.R_OK | fs.constants.F_OK);
  } catch (e) {
    throw new Error('Cannot load the database');
  }
  const database = ((await fs.readFile(path)).toString().split('\n'))
    .filter((elem) => elem.trim() !== '');
  const fields = { CS: [], SWE: [] };

  console.log(`Number of students: ${database.length - 1}`);
  for (let i = 1; i < database.length; i++) {
    const entry = database[i].split(',');
    if (entry[entry.length - 1] in fields) {
      fields[entry[entry.length - 1]].push(entry[0]);
    }
  }
  const studentsCS = fields.CS.join(', ');
  const studentsSWE = fields.SWE.join(', ');
  console.log(
    `Number of students in CS: ${fields.CS.length}. List: ${studentsCS}`
  );
  console.log(
    `Number of students in SWE: ${fields.SWE.length}. List: ${studentsSWE}`
  );
}

module.exports = countStudents;
