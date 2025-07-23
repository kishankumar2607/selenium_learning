const express = require("express");
const app = express();
const server = require("./server");

app.use(server);

const port = 3000;
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
