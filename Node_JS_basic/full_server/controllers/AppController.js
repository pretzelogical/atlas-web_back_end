export default class AppController {
  static getHomepage(request, response) {
    response.set('Content-Type', 'text/plain');
    response.send('Hello Holberton School!');
  }
}
