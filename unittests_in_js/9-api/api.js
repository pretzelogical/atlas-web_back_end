const express = require('express');
const app = express();
const port = 7865;


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

console.log(`API available on localhost port ${port}`);
app.listen(port);
