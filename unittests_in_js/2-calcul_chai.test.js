// import { expect } from 'chai';
// import calculateNumber from './2-calcul_chai.js';
// const assert = require('chai').assert;
const chai = require('chai');
const expect = chai.expect;
const calculateNumber = require('./2-calcul_chai.js');

describe('calculateNumber', function () {
  it('should round numbers from float to integer', function () {

    expect(calculateNumber('SUM', 1.3, 1.7))
      .to.equal(3).and.be.a('number');

    expect(calculateNumber('SUBTRACT', 0.1, 0.1))
      .to.equal(0).and.be.a('number');

    expect(calculateNumber('SUM', 3, 7))
      .to.equal(10).and.be.a('number');

    expect(calculateNumber('DIVIDE', 1.3, 3.7))
      .to.equal(0.25).and.be.a('number');

    const ops = ['SUM', 'SUBTRACT', 'DIVIDE'];
    for (let i = 0; i < 100; i++) {
      const a = Math.random() * 10;
      const b = Math.random() * 10 + 1; // if b is 0 DIVIDE will fail
      const selectedOp = ops[Math.round((Math.random() * 10) % 2)];
      let result;

      if (selectedOp === 'SUM') {
        result = Math.round(a) + Math.round(b);
      } else if (selectedOp === 'SUBTRACT') {
        result = Math.round(a) - Math.round(b);
      } else if (selectedOp === 'DIVIDE') {
        result = Math.round(a) / Math.round(b);
      }
      expect(calculateNumber(selectedOp, a, b))
        .to.equal(result).and.be.a('number');
    }
  });

  it('should error if type is not SUM, SUBTRACT or DIVIDE', function () {
    const errStr = 'Type must be SUM, SUBTRACT or DIVIDE';

    expect(() => calculateNumber('MULTIPLY', 3, 3))
      .to.throw(errStr);

    expect(() => calculateNumber(0, 3, 3))
      .to.throw(errStr);

    expect(() => calculateNumber({}, 3, 3))
      .to.throw(errStr);

  });

  it('should return the string "Error" if type is DIVIDE and b is 0', function () {

    expect(calculateNumber('DIVIDE', 3, 0))
      .to.equal('Error').and.be.a('string');

    expect(calculateNumber('DIVIDE', 3, -99))
      .to.equal('Error').and.be.a('string');

    expect(calculateNumber('DIVIDE', 3, -Infinity))
      .to.equal('Error').and.be.a('string');

  });
});
