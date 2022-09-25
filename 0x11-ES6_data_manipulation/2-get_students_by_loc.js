export default function getStudentsByLocation(arrayobjects, city) {
  if (!(Array.isArray(arrayobjects))) {
    return null;
  }
  return arrayobjects.filter((value) => value.location === city);
}
