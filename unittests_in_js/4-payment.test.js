const sendPaymentRequestToApi = require('./3-payment');
const expect = require('chai').expect;
const sinon = require('sinon');
const Utils = require('./utils.js');

describe('sendPaymentRequestToApi', function() {
  it('Should verify that the math is consistent', () => {
    sinon.spy(Utils, 'calculateNumber');

    expect(sendPaymentRequestToApi(100, 20))
      .to.not.throw;

    expect(Utils.calculateNumber.firstCall.returnValue)
      .to.equal(Utils.calculateNumber('SUM', 100, 20));

    Utils.calculateNumber.restore();
  });

  it('Should stub Utils.calculateNumber to always return 10 and spy on console', () => {
    sinon.stub(Utils, 'calculateNumber').returns(10);
    sinon.spy(console, 'log');

    expect(sendPaymentRequestToApi(100, 20))
      .to.not.throw;
    expect(Utils.calculateNumber.firstCall.args)
      .to.eql(["SUM", 100, 20]);
    expect(console.log.calledWith('The total is: 10'));

    Utils.calculateNumber.restore();
    console.log.restore();
  });
});
