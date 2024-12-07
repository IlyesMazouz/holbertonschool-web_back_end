const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi', function () {
  let consoleSpy;
  let stub;

  beforeEach(function () {
    consoleSpy = sinon.spy(console, 'log');
    
    stub = sinon.stub(Utils, 'calculateNumber').returns(10);
  });

  afterEach(function () {
    consoleSpy.restore();
    stub.restore();
  });

  it('should call Utils.calculateNumber with SUM and log the correct message', function () {
    sendPaymentRequestToApi(100, 20);

    sinon.assert.calledWith(stub, 'SUM', 100, 20);

    sinon.assert.calledWith(consoleSpy, 'The total is: 10');
  });
});
