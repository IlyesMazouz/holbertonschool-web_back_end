export default function appendToEachArrayValue(array, appendString) {
  const modifiedArray = array.map((value) => appendString + value);

  return modifiedArray;
}
