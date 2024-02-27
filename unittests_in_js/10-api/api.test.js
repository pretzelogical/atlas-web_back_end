const request = require('request');
const expect = require('chai').expect;

describe('Index page', () => {
  it('should return reply with "Welcome to the payment system"', () => {
    request.get('http://localhost:7865/', (error, response) => {
      expect(response.body).to.eql('Welcome to the payment system');
    });
  });

  it('should return with response code 200', () => {
    request.get('http://localhost:7865/', (error, response) => {
      expect(response.statusCode).to.equal(200);
    });
  });

  it('should return with Content-Type containing "text/plain"', () => {
    request.get('http://localhost:7865/', (error, response) => {
      expect(response.headers['content-type']).to.contain('text/plain');
    });
  });
});

describe('Cart page', () => {
  it('should return reply with "Payment methods for :id(int)"', () => {
    for (let i = 0; i <= 10; i++) {
      const randID = Math.floor(Math.random() * 100);
      request.get(`http://localhost:7865/cart/${randID}`, (error, response) => {
        expect(response.body).to.eql(`Payment methods for cart ${randID}`);
      });
    }
  });

  it('should return with response code 200', () => {
    request.get('http://localhost:7865/cart/10', (error, response) => {
      expect(response.statusCode).to.equal(200);
    });
  });

  it('should return with response code 404 on non int route', () => {
    request.get('http://localhost:7865/cart/abacab', (error, response) => {
      expect(response.statusCode).to.equal(404);
    });
    request.get('http://localhost:7865/cart/4.0.4', (error, response) => {
      expect(response.statusCode).to.equal(404);
    });
  });
});

describe('Payments page', () => {
  it('should return the available payments in the body', () => {
    request.get(
      'http://localhost:7865/available_payments',
      (error, response) => {
        expect(JSON.parse(response.body)).to.eql({
          payment_methods: {
            credit_cards: true,
            paypal: false,
          },
        });
      }
    );
  });

  it('should return with response code 200', () => {
    request.get(
      'http://localhost:7865/available_payments',
      (error, response) => {
        expect(response.statusCode).to.equal(200);
      }
    );
  });

  it('should return with "Content-Type": "application/json"', () => {
    request.get(
      'http://localhost:7865/available_payments',
      (error, response) => {
        expect(response.headers['content-type']).to.contain('application/json');
      }
    );
  });
});

describe('Login page', () => {
  it('should return the phrase "Welcome ${userName}"', () => {
    request.post(
      'http://localhost:7865/login',
      { json: { userName: 'Betty' } },
      (error, response) => {
        expect(response.body).to.equal('Welcome Betty');
      }
    );
  });

  it('should return with response code 200', () => {
    request.post(
      'http://localhost:7865/login',
      { json: { userName: 'Betty' } },
      (error, response) => {
        expect(response.statusCode).to.equal(200);
      }
    );
  });

  it('should return with Content-Type containing text/plain', () => {
    request.post(
      'http://localhost:7865/login',
      { json: { userName: 'Betty' } },
      (error, response) => {
        expect(response.headers['content-type']).to.contain('text/plain');
      }
    );
  });
});
