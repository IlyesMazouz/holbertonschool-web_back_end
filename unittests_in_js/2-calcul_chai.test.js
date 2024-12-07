const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai.js');

describe('calculateNumber', function () {
  describe('SUM', function () {
    it('should return 6 when a is 1.4 and b is 4.5', function () {
      expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });

    it('should return 0 when a is 0.2 and b is -0.5', function () {
      expect(calculateNumber('SUM', 0.2, -0.5)).to.equal(0);
    });
  });

  describe('SUBTRACT', function () {
    it('should return -4 when a is 1.4 and b is 4.5', function () {
      expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    });

    it('should return -1 when a is -0.2 and b is 0.5', function () {
      expect(calculateNumber('SUBTRACT', -0.2, 0.5)).to.equal(-1);
    });
  });

  describe('DIVIDE', function () {
    it('should return 0.2 when a is 1.4 and b is 4.5', function () {
      expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    });

    it('should return "Error" when b is 0', function () {
      expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });

    it('should return 2 when a is 5.5 and b is 2.5', function () {
      expect(calculateNumber('DIVIDE', 5.5, 2.5)).to.equal(2);
    });
  });

  describe('Invalid type', function () {
    it('should return "Invalid type" when an invalid type is passed', function () {
      expect(calculateNumber('MULTIPLY', 1.4, 4.5)).to.equal('Invalid type');
    });
  });
});
