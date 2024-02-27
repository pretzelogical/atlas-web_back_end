const express = require('express');
const app = express();
const port = 7865;

app.use(express.json());

app.get('/', (req, res) => {
  res.type('text/plain');
  res.send('Welcome to the payment system');
  res.end();
});

app.get('/cart/:id(\\d+)', (req, res) => {
  res.type('text/plain');
  res.send(`Payment methods for cart ${req.params['id']}`);
  res.end();
});

app.get('/available_payments', (req, res) => {
  res.type('application/json');
  res.send(JSON.stringify({
    'payment_methods': {
      'credit_cards': true,
      'paypal': false
    }
  }));
  res.end();
});

app.post('/login', (req, res) => {
  res.type('text/plain');
  res.send(`Welcome ${req.body.userName}`);
  res.end();
})

console.log(`API available on localhost port ${port}`);
app.listen(port);
