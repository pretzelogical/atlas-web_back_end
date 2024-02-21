#!/usr/bin/env node
const http = require("http");
const countStudents = require("./3-read_file_async");

const app = http.createServer((req, res) => {
    res.writeHead(200, { "Content-Type": "text/plain" });
    const studentsResponse = [
      "This is the list of our students",
      "Number of students: 10",
      "Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie",
      "Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy",
    ];
    let response = "Hello Holberton School!";
    if (req.url === "/students") {
      response = studentsResponse.join("\n");
    }
    res.write(response);
    res.end();
  }).listen(1245);

module.exports = app;
