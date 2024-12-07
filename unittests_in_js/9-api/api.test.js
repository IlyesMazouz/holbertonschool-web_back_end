const request = require('request');

describe('Index page', function() {
  let server;

  before(function(done) {
    server = require('./api.js');
    done();
  });

  it('should return correct status code', function(done) {
    request.get('http://localhost:7865', (err, res, body) => {
      if (err) return done(err);
      res.statusCode.should.equal(200);
      done();
    });
  });

  it('should return correct result', function(done) {
    request.get('http://localhost:7865', (err, res, body) => {
      if (err) return done(err);
      body.should.equal('Welcome to the payment system');
      done();
    });
  });

  describe('Cart page', function() {
    it('should return correct status code when :id is a number', function(done) {
      request.get('http://localhost:7865/cart/12', (err, res, body) => {
        if (err) return done(err);
        res.statusCode.should.equal(200);
        body.should.equal('Payment methods for cart 12');
        done();
      });
    });

    it('should return correct status code when :id is NOT a number', function(done) {
      request.get('http://localhost:7865/cart/hello', (err, res, body) => {
        if (err) return done(err);
        res.statusCode.should.equal(404);
        body.should.equal('Cart not found');
        done();
      });
    });
  });

  after(function(done) {
    server.close();
    done();
  });
});
