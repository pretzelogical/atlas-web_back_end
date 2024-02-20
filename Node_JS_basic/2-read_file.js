#!/usr/bin/env node
const fs = require("fs");
const readline = require("readline");

function countStudents(path) {
  if (!fs.existsSync(path)) {
    throw new Error("Cannot load the database");
  }

  const databaseBytes = fs.readFileSync(path);
  const database = databaseBytes.toString().split("\n");
  let lineNum = 0;
  let fields = {};

  for (const entry of database) {
    if (lineNum == 0) {
      lineNum++;
      continue;
    }
    student = entry.split(",");
    studentField = student[student.length - 1];
    if (studentField in fields) {
      fields[studentField].push(student[0]);
    } else {
      fields[studentField] = [student[0]];
    }
    lineNum++;
  }
  const csStudents = fields["CS"].join(", ");
  const sweStudents = fields["SWE"].join(", ");
  console.log(`Number of students: ${lineNum - 1}`);
  console.log(
    `Number of students in CS: ${fields["CS"].length}. List: ${csStudents}`
  );
  console.log(
    `Number of students in SWE: ${fields["SWE"].length}. List: ${sweStudents}`
  );
}

module.exports = countStudents;
