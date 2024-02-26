const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('calculateNumber', function() {

  it('should round numbers from float to integer', function() {
    assert.strictEqual(calculateNumber('SUM', 1.3, 1.7), 3);
    assert.strictEqual(calculateNumber('SUBTRACT', 0.1, 0.1), 0);
    assert.strictEqual(calculateNumber('SUM', 3, 7), 10);
    assert.strictEqual(calculateNumber('DIVIDE', 1.3, 3.7), 0.25);

    const ops = ['SUM', 'SUBTRACT', 'DIVIDE'];
    for (let i = 0; i < 100; i++) {
      const a = Math.random() * 10;
      const b = (Math.random() * 10) + 1; // if b is 0 DIVIDE will fail
      const selectedOp = ops[Math.round((Math.random() * 10) % 2)];
      let result;

      if (selectedOp === 'SUM') {
        result = Math.round(a) + Math.round(b);
      } else if (selectedOp === 'SUBTRACT') {
        result = Math.round(a) - Math.round(b);
      } else if (selectedOp === 'DIVIDE') {
        result = Math.round(a) / Math.round(b);
      }
      assert.strictEqual(calculateNumber(selectedOp, a, b), result);
    }
  });

  it('should error if type is not SUM, SUBTRACT or DIVIDE', function() {
    const err = new Error('Type must be SUM, SUBTRACT or DIVIDE');
    assert.throws(() => calculateNumber('MULTIPLY', 3, 3), err);
    assert.throws(() => calculateNumber(0, 3, 3), err);
    assert.throws(() => calculateNumber({}, 3, 3), err);
  });

  it('should return the string "Error" if type is DIVIDE and b is 0', function() {
    assert.strictEqual(calculateNumber('DIVIDE', 3, 0), 'Error');
    assert.strictEqual(calculateNumber('DIVIDE', 3, -99), 'Error');
    assert.strictEqual(calculateNumber('DIVIDE', 3, -Infinity), 'Error');
  });
});
