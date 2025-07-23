const express = require("express");
const app = express();
const sqlite = require("sqlite3").verbose();

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Database Connection
const db = new sqlite.Database("./database.db");
db.serialize(function () {
  db.run(
    "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)"
  );

  db.run("DELETE FROM users");

  db.run("INSERT INTO users (username, password) VALUES ('admin', 'password')");
});

// Default Router Message
app.get("/", (req, res, next) => {
  res.send(
    `<form method="POST" action="/login">
      <h2>Login Form</h2>
      <label for="username">Username:</label>
      <input type="text" id="username" name="username" required />
      <br/><br/>
      <label for="password">Password:</label>
      <input type="password" id="password" name="password" required />
      <br/><br />
      <button type="submit">Login</button>
    </form>`
  );
});

app.post("/login", (req, res, next) => {
  const { username, password } = req.body;
  // const query = `SELECT * FROM users WHERE username = '${username}' AND password = '${password}'`;

  //protect from sql injection
  const query = `SELECT * FROM users WHERE username = ? AND password = ?`;
  // db.prepare(query)
  //   .bind(username, password)
  //   .get((err, row) => {
  //     if (err) {
  //       console.error(err);
  //       res.status(500).send("Error");
  //     } else if (row) {
  //       res.send(`Welcome, ${username}!`);
  //     } else {
  //       res.status(401).send("Invalid username or password");
  //     }
  //   });

  db.all(query, (err, rows) => {
    if (err) {
      console.error(err.message);
      return res.send("Internal Server Error");
    }
    if (rows.length > 0) {
      return res.send("Login Successful");
    } else {
      return res.send("Login Failed");
    }
  });
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
