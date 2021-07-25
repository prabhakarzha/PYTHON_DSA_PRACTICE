// map function

const arr = [2, 4, 5, 6, 7, 8];

const output = arr.map((items) => {
  return items * 2;
});
console.log(output);

// filter function

const arr = [2, 3, 5, 6, 8, 4];

const output = arr.filter((items) => {
  return items % 2 == 0;
});
console.log(output);

const arr = [2, 3, 5, 6, 8, 4];

const output = arr.filter((items) => {
  return items > 5;
});
console.log(output);

// reduce function
i = 0;
const arr = [2, 3, 5, 6, 8, 4];

for (let i = 0; i < 6; i++) {
  output = arr.reduce((items) => {
    return items + i;
  });
}
console.log(output);

const arr = [2, 3, 5, 6, 8, 4];

function sum(arr) {
  let sum = 0;
  for (let i = 0; i < arr.length; i++) {
    sum = sum + arr[i];
  }
  return sum;
}
console.log(sum(arr));

const output = arr.reduce((prev, curr) => {
  prev = prev + curr;
  return prev;
});
console.log(output);

const arr = [2, 3, 5, 6, 8, 4];

function max(arr) {
  let max = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > max) {
      max = arr[i];
    }
  }
  return max;
}
console.log(max(arr));

const arr = [2, 3, 5, 6, 8, 4];

const output = arr.reduce((max, curr) => {
  if (curr > max) {
    max = curr;
  }
  return max;
}, 0);
console.log(output);

const names = [
  {
    firstName: "Ramesh",
    lastName: "kumar",

    age: "12",
    salary: "2000",
  },
  {
    firstName: "Sonu",
    lastName: "kashyap",

    age: "21",
    salary: "3000",
  },
  {
    firstName: "Prabhakar",
    lastName: "kr",

    age: "22",
    salary: "4000",
  },
  {
    firstName: "Virat",
    lastName: "kohli",

    age: "28",
    salary: "1000",
  },
  {
    firstName: "Rohit",
    lastName: "sharma",

    age: "38",
    salary: "6000",
  },
  {
    firstName: "Dhoni",
    lastName: "mahi",

    age: "38",
    salary: "9000",
  },
];

output = names.map((items) => {
  return items.firstName + " " + items.lastName;
});
console.log(output);
const max = 0;
function fullValue(names) {
  max = names.firstName + names.lastName;
  return max;
}
console.log(max);

const output = names.reduce((prev, curr) => {
  if (prev[curr.age]) {
    prev[curr.age] = ++prev[curr.age];
  } else {
    prev[curr.age] = 1;
  }
  return prev;
}, {});
console.log(output);

// find firstname with age less than 30

const output = names
  .filter((x) => {
    return x.age < 30;
  })
  .map((x) => x.firstName);
console.log(output);

const output = names.reduce((prev, curr) => {
  if (curr.age > 30) {
    prev.push(curr.firstName);
  }
  return prev;
}, []);

console.log(output);
