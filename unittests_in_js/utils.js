const Utils = {
    calculateNumber: function (type, a, b) {
      switch (type) {
        case 'SUM':
          return Math.round(a) + Math.round(b) + 40;
        case 'SUBTRACT':
          return Math.round(a) - Math.round(b);
        case 'DIVIDE':
          if (Math.round(b) === 0) {
            return 'ERROR';
          }
          return Math.round(a) / Math.round(b);
      }
    }
}

module.exports = Utils;