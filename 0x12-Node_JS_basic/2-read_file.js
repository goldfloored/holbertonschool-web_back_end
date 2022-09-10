const fs = require('fs');

module.exports = function countStudents(path) {
  let data;
  try {
    data = fs.readFileSync(path);
  } catch (error) {
    throw new Error('Cannot load the database');
  }

  data = data.toString().split('\n');
  data = data.filter((elem) => elem.length > 0);
  data.shift();
  console.log(`Number of students: ${data.length}`);
  const fields = {};
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
  for (const field in fields) {
    if (field) {
      const res = fields[field];
      console.log(`Number of students in ${field}: ${res.length}. List: ${res.join(', ')}`);
    }
  }
};
