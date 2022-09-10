const http = require('http');
const dbfile = require('./3-read_file_async');

const app = http.createServer(async (req, res) => {
  res.statusCode = 200;
  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    await dbfile(process.argv[2])
      .then((success) => {
        const output = `This is the list of our students\n${success}`;
        res.end(output);
      })
      .catch((err) => {
        res.write('This is the list of our students\n');
        res.end(err.message);
      });
  }
}).listen(1245);

module.exports = app;
