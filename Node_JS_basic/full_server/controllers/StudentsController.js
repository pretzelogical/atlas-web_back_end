import readDatabase from '../utils';
import fs from 'fs/promises';

export default class StudentsController {
  static async getAllStudents(request, response) {
    response.set('Content-Type', 'text/plain');
    try {
      const database = await readDatabase(process.argv[2]);
    } catch (err) {
      response.status(500).send('Cannot load the database');
      return;
    }
    const message = ['This is the list of our students'];

    for (const field in database) {
      let line = `Number of students in ${field}: ${database[field].length}.`;
      line += ` List: ${database[field].join(', ')}`;
      message.push(line);
    }
    response.status(200).send(message.join('\n'));
  }
  static async getAllStudentsByMajor(request, response) {
    response.set('Content-Type', 'text/plain');
    try {
      const database = await readDatabase(process.argv[2]);
    } catch (err) {
      response.status(500).send('Cannot load the database');
      return;
    }
    const major = request.params.major;
    if (!['CS', 'SWE'].includes(major)) {
      response.status(500).send('Major parameter must be CS or SWE');
      return;
    }
    response.status(200).send(`List: ${database[major].join(', ')}`);
  }
}
