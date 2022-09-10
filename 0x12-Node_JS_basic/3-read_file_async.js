const fs = require('fs');

module.exports = function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, (error, dataFile) => {
      if (error) {
        reject(Error('Cannot load the database'));
      }
      if (dataFile) {
        const fields = {};
        let data = dataFile.toString().split('\n');
        data = data.filter((elem) => elem.length > 0);
        data.shift();

        data.forEach((elem) => {
          if (elem.length > 0) {
            const value = elem.split(',');
            if (value[3] in fields) {
              fields[value[3]].push(value[0]);
            } else {
              fields[value[3]] = [value[0]];
            }
          }
        });
        console.log(`Number of students: ${data.length}`);
        for (const field in fields) {
          if (field) {
            const res = fields[field];
            console.log(`Number of students in ${field}: ${res.length}. List: ${res.join(', ')}`);
          }
        }
      }
      resolve();
    });
  });
};
