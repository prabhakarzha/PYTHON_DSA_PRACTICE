// arr = [4, 5, 2, 3, 1, 8, 12, 6];
// arr1 = [];
// n = arr.length;
// for (let i = n - 1; i >= 0; i--) {
//   arr1.push(arr[i]);
// }
// console.log(arr1);

arr = [4, 5, 2, 3, 1, 8, 12, 6];
arr1 = [];
arr.forEach((e) => {
  arr1.unshift(e);  //unshift method is similar to push 
});
console.log(arr1);

