const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./5-payment');
const { assert } = require('chai');

describe('sendPaymentRequestToApi', function () {
  let consoleSpy;

  beforeEach(function () {
    consoleSpy = sinon.spy(console, 'log');
  });

  afterEach(function () {
    consoleSpy.restore();
  });

  it('should log the correct total when passed 100 and 20', function () {
    sendPaymentRequestToApi(100, 20);

    assert(consoleSpy.calledWith('The total is: 120'));

    assert(consoleSpy.calledOnce);
  });

  it('should log the correct total when passed 10 and 10', function () {
    sendPaymentRequestToApi(10, 10);

    assert(consoleSpy.calledWith('The total is: 20'));

    assert(consoleSpy.calledOnce);
  });
});

if (require.main === module) {
  require('mocha').run();
}
