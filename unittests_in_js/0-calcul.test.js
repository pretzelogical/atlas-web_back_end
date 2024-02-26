const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', function() {
  it('Should round numbers from float to integer', function() {
    assert.strictEqual(calculateNumber(1.3, 1.7), 3);
    assert.strictEqual(calculateNumber(0.1, 0.1), 0);
    assert.strictEqual(calculateNumber(3, 7), 10);
    assert.strictEqual(calculateNumber(1.3, 1.7), 3);
    for (let i = 0; i < 10; i++) {
      const a = Math.random() * 10;
      const b = Math.random() * 10;
      assert.strictEqual(calculateNumber(a, b), Math.round(a) + Math.round(b));
    }
  });
});
