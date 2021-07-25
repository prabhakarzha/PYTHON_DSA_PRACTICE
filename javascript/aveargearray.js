const mathClass = [
  {
    name: "Sonu",
    grade: "60",
    age: "22",
  },
  {
    name: "Prabhakar",
    grade: "90",
    age: "21",
  },
];

const englishClass = [
  {
    name: "Sonu",
    grade: "60",
    age: "22",
  },
  {
    name: "Virat",
    grade: "80",
    age: "31",
  },
];
const getAverageByCondition = (arr,func)=>
      arr.map(typeof func === 'function'? func:val=>[func])
      .reduce((acc,val)=>acc+val,0)/arr.length;

getAverageByCondition(englishClass,'grade')
getAverageByCondition(mathClass,el=>el.grade)

console.log(englishClass,mathClass);


