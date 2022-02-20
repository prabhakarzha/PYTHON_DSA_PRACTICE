// const number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16];
// const values = number.filter((n) => {
//   return n % 2 != 0;
// });
// console.log(values);

const bcom = [
  {
    name: "kanhai",
    percent: 75,
  },
  {
    name: "ravi",
    percent: 23,
  },
  {
    name: "prabhast",
    percent: 65,
  },
  {
    name: "rishu",
    percent: 16,
  },
  {
    name: "sonu",
    percent: 87,
  },
];
const result = bcom.filter((n) => {
  return n.percent >= 80;
});
console.log(result);
