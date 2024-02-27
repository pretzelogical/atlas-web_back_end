const Utils = {
  calculateNumber(type, a, b) {
    a = Math.round(a);
    b = Math.round(b);
    const ops = {
      'SUM': () => a + b,
      'SUBTRACT': () => a - b,
      'DIVIDE': () => {
        if (b <= 0) {
          return 'Error';
        }
        return a / b;
      }
    }
    if (type in ops === false) {
      throw new Error('Type must be SUM, SUBTRACT or DIVIDE');
    }
    return ops[type](a, b);
  }
}

module.exports = Utils;
