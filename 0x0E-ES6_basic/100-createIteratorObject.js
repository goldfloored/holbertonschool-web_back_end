export default function createIteratorObject(report) {
    const employee = [];
    for (const name of Object.keys(report.allEmployees)) {
      employee.push(...report.allEmployees[name]);
    }
    return employee;
  }