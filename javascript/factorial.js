// function fact(num) {
//   return num;
// }
// console.log(factorialize(5));

// function factorialize(num) {
//   if (num < 0)
//   return -1;
//   else if (num == 0)
//   return 1;
//   else {
//     return num * factorialize(num - 1);
//   }
// }
// const result = factorialize(5);
// console.log(result);

function factorialize(num) {
  var result = num;
  if (num === 0 || num === 1) return 1;

  while (num > 1) {
    num--;
    result = result * num;
  }
  return result;
}
const res = factorialize(5);
console.log(res);
// function
