// problem no-1 checking sum zero

// function checkSum(array){
//     for(let num of array){
//         for(let j = 1; j < array.length; j++){
//             if(num+array[j]===0){
//                 return [num,array[j]];
//             }
//         }
//     }
// }
// const result =checkSum([-5,-4,-3,-2,0,2,4,6,8]);
// console.log(result);

function checkSum(array) {
  let left = 0;
  let right = array.length - 1;

  while (left < right) {
    sum = array[left] + array[right];
    if (sum === 0) {
      return [array[left], array[right]];
    } else if (sum > 0) {
      right--;
    } else {
      left++;
    }
  }
}
const result = checkSum([-5, -4, -3, -2, 0, 2, 4, 6, 8]);
console.log(result);
