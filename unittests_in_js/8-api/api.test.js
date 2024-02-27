const request = require('request');
const expect = require('chai').expect;


describe('Index page', () => {
  it('should return reply with "Welcome to the payment system"', () => {
    request.get('http://localhost:7865/', (error, response, body) => {
      expect(response.body).to.eql('Welcome to the payment system');
    })
  });

  it('should return with response code 200', () => {
    request.get('http://localhost:7865/', (error, response, body) => {
      expect(response.statusCode).to.equal(200);
    })
  });

  it('should return with Content-Type containing "text/plain"', () => {
    request.get('http://localhost:7865/', (error, response, body) => {
      expect(response.headers['content-type']).to.contain('text/plain');
    })
  });
});