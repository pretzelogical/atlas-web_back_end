const sendPaymentRequestToApi = require('./3-payment');
const expect = require('chai').expect;
const sinon = require('sinon');
const Utils = require('./utils.js');

describe('sendPaymentRequestToApi', function() {
  it('Should verify that the math is consistent', function() {

    sinon.spy(Utils, 'calculateNumber');

    expect(sendPaymentRequestToApi(100, 20))
      .to.not.throw;

    expect(Utils.calculateNumber.firstCall.returnValue)
      .to.equal(120);

    Utils.calculateNumber.restore();

  });
});
