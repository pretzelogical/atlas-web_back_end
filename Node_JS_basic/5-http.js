#!/usr/bin/env node
const http = require('http');
const fs = require('fs/promises');

async function countStudents(path) {
  try {
    await fs.access(path, fs.constants.R_OK | fs.constants.F_OK);
  } catch (e) {
    throw new Error('Cannot load the database');
  }
  const database = (await fs.readFile(path)).toString().split('\n');
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
    `Number of students ${database.length - 1}`,
    `Number of students in CS: ${fields.CS.length} List: ${studentsCS}`,
    `Number of students in SWE: ${fields.SWE.length} List: ${studentsSWE}`
  ];
}

const app = http
  .createServer(async (req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    let response = 'Hello Holberton School!';
    if (req.url === '/students') {
      response = (await countStudents(process.argv[2])).join('\n');
    }
    res.write(response);
    res.end();
  })
  .listen(1245);

module.exports = app;
