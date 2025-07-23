const express = require("express");
const bodyParser = require('body-parser');
const app = express();

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

// Dummy credentials
const correctUsername = 'admin';
const correctPassword = '1234';

// Serve the form on browser
app.get('/', (req, res) => {
  res.send(`
    <h2>🔐 Demo Login Form</h2>
    <form method="POST" action="/login">
      <label>Username:</label><br/>
      <input name="username" value="admin" /><br/>
      <label>Password:</label><br/>
      <input name="password" type="password" /><br/><br/>
      <button type="submit">Login</button>
    </form>
  `);
});

// Accept login
app.post('/login', (req, res) => {
  const { username, password } = req.body;

  if (username === correctUsername && password === correctPassword) {
    return res.send('✅ Login successful!');
  } else {
    return res.status(401).send('❌ Invalid credentials.');
  }
});

// For Throwing error about not found
app.use(async (req, res, next) => {
  next(createError.NotFound("This route does not exist"));
});

// Error Handler
app.use(async (error, req, res, next) => {
  res.status(error.status || 500);
  res.send({
    error: {
      status: error.status || 500,
      message: error.message,
    },
  });
});

// Export the Express API
module.exports = app;
