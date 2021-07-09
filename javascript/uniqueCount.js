function countUnique(array) {
  if (array.length > 0) {
    let i = 0;
    for (let j = 1; j < array.length; j++) {
      if (array[i] !== array[j]) {
        i++;
        array[i] = array[j];
      }
    }
    return i + 1;
  }
}
const result = countUnique([1, 1, 2, 2, 3, 4, 4, 5, 6, 7, 8, 8]);
console.log(result);




// using set 

let arr=[1,1,2,2,3,3,4,5,6,7,7,7,8];
let Arr=new Set(arr);
console.log("unique Count",Arr.size);