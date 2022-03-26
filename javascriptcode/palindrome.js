// str = "sonu";
// v = str.split("").reverse().join("");
// console.log(v);

function Palindrome(str) {
  let newStr = str.toLowerCase();

  let left = 0;
  let right = newStr.length - 1;
  while (left < right) {
    if (newStr[left] !== newStr[right]) return false;
    left++;
    right--;
  }
  return true;
}
console.log(Palindrome("naman")); 

