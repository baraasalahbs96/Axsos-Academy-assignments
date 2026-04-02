let colors = ["red", "blue", "green", "yellow", "purple"];
console.log("The first element is", colors[0], "and last element is", colors[colors.length - 1])
console.log("The element at the second position is", colors[1])
colors[2] = "orange";
console.log(colors)
// 
let numbers = [10, 20, 30, 40, 50];
console.log("Traversing The Array")
for (var i = 0; i < numbers.length; i++) {
    console.log(numbers[i]);
}
console.log("Reversing The Array")
for (var i = numbers.length - 1; i >= 0; i--) {
    console.log(numbers[i]);
}
// 
let numbers2 = [5, 10, 15, 20, 25];
var print = "";
    if (numbers2.includes(25)) {
        print = "Found at position " + numbers2.indexOf(25);
    }
    else {
        print = "Not Found";
    }
console.log(print);
// 
console.log("Ascending sort")
scores.sort((a, b) => a - b)
console.log(scores)
console.log("Descending sort")
scores.sort((a, b) => b - a)
console.log(scores)
// 
let names = ["Shatha", "Sara", "Lina", "Sami", "Dalia"];
console.log("Alphabetical order")
names.sort();
console.log(names)
// 
let animals = ["dog", "cat", "rabbit"]
animals.push("elephant")
console.log(animals)
animals.unshift("lion")
console.log(animals)
animals.splice(2, 0, "tiger")
console.log(animals)
// 
let fruits = ["apple", "banana", "cherry", "date"]
fruits.pop()
console.log(fruits)
let fruits2 = ["apple", "banana", "cherry", "date"]
fruits2.shift()
console.log(fruits2)
let fruits3 = ["apple", "banana", "cherry", "date"]
fruits3.splice(1, 1)
console.log(fruits3)
// 
let array1 = [1, 2, 3];
let array2 = [4, 5, 6];
combinedArray = [
    [1, 2, 3],
    [4, 5, 6]
];
for (var i = 0; i < combinedArray.length; i++) {
    for (var j = 0; j < combinedArray[i].length; j++) {
        console.log(combinedArray[i][j])
    }
}
console.log("Another solution")
let arr1 = [1, 2, 3];
let arr2 = [4, 5, 6];
let combined = [...arr1, ...arr2];
console.log(combined);
// 
let items = ["a", "b", "c", "d", "e"]
let midIndex = Math.ceil(items.length / 2)
let firstArray = items.slice(0, midIndex)
let secondArray = items.slice(midIndex)
console.log(firstArray)
console.log(secondArray)
// 
let numbers3 = [1, 5, 10, 15, 20, 25, 30]
let filteredArray = numbers3.filter(function (num) {
    return num > 15;
});
let filteredArray2 = numbers3.filter(x => x > 15);
console.log(filteredArray)
console.log(filteredArray2)
// 
let unique = [];
for (var i = 0; i < inputs.length; i++) { //for (let num of numbers)
    if (!unique.includes(inputs[i])) {
        unique.push(inputs[i]);
    }
}
console.log(unique);
// 
var inputs2 = [1, 2, 3, 4, 5];
var n = 2;
for (var i = 0; i < n; i++) {
    let x = inputs2.pop();
    inputs2.unshift(x);
}
console.log(inputs2)
// 
let outputArray = [...inputArrays[0], ...inputArrays[1]];
console.log("Combined array before sort: " + outputArray);
for (let i = 0; i < outputArray.length; i++) {
    for (let j = 0; j < outputArray.length - 1; j++) {
        if (outputArray[j] > outputArray[j + 1]) {
            let temp = outputArray[j];
            outputArray[j] = outputArray[j + 1];
            outputArray[j + 1] = temp;
        }
    }
}
console.log("The sorted combined array is: ");
console.log(outputArray);