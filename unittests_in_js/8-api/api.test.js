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

  after(function(done) {
    server.close();
    done();
  });
});
