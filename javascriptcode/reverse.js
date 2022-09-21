function reverseNum(num) {
  let first = 0;
  let last = num.length - 1;
  while (first < last) {
    let temp = num[last];
    num[last] = num[first];
    num[first] = temp;
    first++;
    last--;
  }
}
let num = [1, 2, 3, 4, 5, 6];
reverseNum(num);
console.log(num);


