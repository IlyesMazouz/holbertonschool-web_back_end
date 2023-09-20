export default function appendToEachArrayValue(array, appendString) {
  const modifiedArray = [];

  for (const value of array) {
    modifiedArray.push(appendString + value);
  }

  return modifiedArray;
}
