#!/usr/bin/env node
const fs = require('fs').promises;

export default async function readDatabase (path) {
  try {
    await fs.access(path, fs.constants.F_OK | fs.constants.R_OK);
  } catch (err) {
    throw new Error('Cannot load the database');
  }
  const database = ((await fs.readFile(path)).toString()).split('\n')
    .filter((elem) => elem.trim() !== '');
  const fields = { CS: [], SWE: [] };

  for (let i = 1; i < database.length; i++) {
    const entry = database[i].split(',');
    if (entry[entry.length - 1] in fields) {
      fields[entry[entry.length - 1]].push(entry[0]);
    }
  }
  return fields;
}
