const sendPaymentRequestToApi = require('./4-payment');
const expect = require('chai').expect;
const sinon = require('sinon');
const Utils = require('./utils.js');

describe('sendPaymentRequestToAPI', () => {
  beforeEach(() => {
    sinon.spy(console, 'log');
  });

  afterEach(() => {
    console.log.restore();
  });

  it('should verify the console is logging the string "The total is: 120" once', () => {
    sendPaymentRequestToApi(100, 20);

    expect(console.log.calledOnce).to.eql(true);
    expect(console.log.calledOnceWith('The total is: 120')).to.eql(true);
  });

  it('should verify the console is logging the string "The total is: 20" once', () => {
    sendPaymentRequestToApi(10, 10);

    expect(console.log.calledOnce).to.eql(true);
    expect(console.log.calledOnceWith('The total is: 20')).to.eql(true);
  });
});