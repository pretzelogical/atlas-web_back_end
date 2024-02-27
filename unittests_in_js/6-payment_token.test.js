const sendPaymentRequestToApi = require('./4-payment');
const expect = require('chai').expect;
const sinon = require('sinon');
const getPaymentTokenFromAPI = require('./6-payment_token');


describe('getPaymentTokenFromAPI', () => {
  it('Tests the return values', (done) => {
    getPaymentTokenFromAPI(true).then((data) => {
      expect(data).to.eql({ 'data': 'Successful response from the API' });
    });

    getPaymentTokenFromAPI(false).then((data) => {
      expect(data).to.eql(undefined);
    });

    done();
  });
});
