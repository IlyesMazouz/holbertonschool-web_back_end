const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./5-payment');

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

    sinon.assert.calledWith(consoleSpy, 'The total is: 120');
    
    sinon.assert.calledOnce(consoleSpy);
  });

  it('should log the correct total when passed 10 and 10', function () {
    sendPaymentRequestToApi(10, 10);

    sinon.assert.calledWith(consoleSpy, 'The total is: 20');
    
    sinon.assert.calledOnce(consoleSpy);
  });
});
