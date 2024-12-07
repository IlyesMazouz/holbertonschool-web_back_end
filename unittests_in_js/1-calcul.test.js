const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('calculateNumber', function () {
  describe('SUM', function () {
    it('should return 6 when a is 1.4 and b is 4.5', function () {
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });

    it('should return 0 when a is 0.2 and b is -0.5', function () {
      assert.strictEqual(calculateNumber('SUM', 0.2, -0.5), 0);
    });
  });

  describe('SUBTRACT', function () {
    it('should return -4 when a is 1.4 and b is 4.5', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });

    it('should return -1 when a is -0.2 and b is 0.5', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', -0.2, 0.5), -1);
    });
  });

  describe('DIVIDE', function () {
    it('should return 0.2 when a is 1.4 and b is 4.5', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });

    it('should return "Error" when b is 0', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });

    it('should return 2 when a is 5.5 and b is 2.5', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 5.5, 2.5), 2);
    });
  });

  describe('Invalid type', function () {
    it('should return "Invalid type" when an invalid type is passed', function () {
      assert.strictEqual(calculateNumber('MULTIPLY', 1.4, 4.5), 'Invalid type');
    });
  });
});
