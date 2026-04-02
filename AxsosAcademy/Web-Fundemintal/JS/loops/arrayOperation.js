// 1. Accessing Elements
// a. Create an array let colors = ["red", "blue", "green", "yellow", "purple"];.
let colors = ["red", "blue", "green", "yellow", "purple"];
// Print the first and last elements of the array.
console.log(color[0]);
console.log(colors[4]);
// Print the element at the second position.
console.log(colors[1]);
// Update the third element to orange and print the updated array.
color[2]="orange";
console.log(colors);
// 2. Traversing an Array
// a. Given the array let numbers = [10, 20, 30, 40, 50];, write a program to print each element using a for loop.
let numbers= [10, 20, 30, 40, 50];
for (i=0; i<numbers.length; i++){
    console.log(numbers[i]);
}
// b. Write a for loop to print the elements in reverse order.
let numbers= [10, 20, 30, 40, 50];
for (i=numbers.length-1; i>=0; i--){
    console.log(numbers[i]);
}
// 3. Searching in an Array
// a. Write a program to check if the number 25 exists in the array let numbers = [5, 10, 15, 20, 25];.
// If it exists, print "Found at position X".
// If it doesn’t exist, print "Not Found".
let numbers = [5, 10, 15, 20, 25];
let num= numbers.indexOf(25);
if (num!== -1) {
    console.log("Found at position X");
}else{
     console.log("Not Found");
}
// 4. Sorting an Array
// a. Write a program to sort the array let scores = [50, 20, 70, 10, 40]; in:

// Ascending order
let scores = [50, 20, 70, 10, 40];
scores.sort((a,b)=>(a-b));
console.log(scores);
// Descending order
let scores = [50, 20, 70, 10, 40];
scores.sort((a,b)=>(b-a));
console.log(scores);
// b. Sort the array let names = ["Shatha", "Sara", "Lina", "Sami", "Dalia"]; in alphabetical order.
let names = ["Shatha", "Sara", "Lina", "Sami", "Dalia"];
names.sort();
console.log(names);

// 5. Inserting Elements
// a. Given the array let animals = ["dog", "cat", "rabbit"];:
// Add "elephant" to the end of the array.
let animals =["dog", "cat", "rabbit"];
animals.push("elephant");
console.log(animals);
// Add "lion" to the beginning of the array.
let animals =["dog", "cat", "rabbit"];
animals.unshift("lion");
console.log(animals);
//  Insert "tiger" between "dog" and "cat".
let animals =["dog", "cat", "rabbit"];
animals.splice(2,0,"tiger");
console.log(animals);
// 6. Deleting Elements
// a. Given the array let fruits = ["apple", "banana", "cherry", "date"];:
// Remove the first element.
let fruits = ["apple", "banana", "cherry", "date"];
fruits.shift();
console.log(fruits);
// Remove the last element.
let fruits = ["apple", "banana", "cherry", "date"];
fruits.pop();
console.log(fruits);
//  Remove "banana" from the array without using its index directly.
let fruits = ["apple", "banana", "cherry", "date"];
fruits.splice(1,1)
console.log(fruits);
// 7. Combining Arrays
// a. Given two arrays:
// let array1 = [1, 2, 3];
// let array2 = [4, 5, 6];
// Combine them into a single array.
// Print the combined array.
let array1 = [1, 2, 3];
let array2 = [4, 5, 6];
let combine= array1.concat(array2);
console.log(combine);
// 8. Splitting an Array
// a. Given the array let items = ["a", "b", "c", "d", "e"];, split it into two arrays:
// The first three elements go into one array.
// The rest go into another array.
let items = ["a", "b", "c", "d", "e"];
let firstArray=items.slice(0,3);
let secondArray=items.slice(3);
console.log(firstArray);
console.log(secondArray)

// 9. Filtering Elements
// a. Given the array let numbers = [1, 5, 10, 15, 20, 25, 30];:
// Create a new array containing only numbers greater than 15.
// Print the filtered array.
let numbers = [1, 5, 10, 15, 20, 25, 30];
let greaterNum= numbers.filter(n=> n>15);
console.log(greaterNum);
// 10. Advanced Challenge
// a. Write a program to remove duplicate elements from an array.
// Example:
// Input: [1, 2, 2, 3, 4, 4, 5]  
// Output: [1, 2, 3, 4, 5]
function removeDuplicate(arr){
    let result=[];
    for (let i=0, i<arr.length; i++){
        if (!result.includes(arr[i])){
            result.push(arr[i]);
        }
    }
    return result;
}
console.log(removeDuplicate([1,2,2,3,4,4,5]))
// b. Write a program to rotate an array to the right by n positions.
// Example:
// Input: [1, 2, 3, 4, 5], n = 2  
// Output: [4, 5, 1, 2, 3]
function rotateRight(arr, n){
    for (let i=0; i<n; i++){
        let lastNum=arr.pop();
        arr.unshift(lastNum);
    }
    return arr;
}
console.log(rotateRight([1,2,3,4,5],2));
// Bonus Challenge
// Write a program to merge two sorted arrays into a single sorted array without using the built-in sort() function.
// Example:
// Input: [1, 3, 5], [2, 4, 6]  
// Output: [1, 2, 3, 4, 5, 6]
arr1=[1, 3, 5]
arr2=[2, 4, 6]
function merge(arr1,arr2){
    let i=0;
    let j=0;
    let result=[];

    while (i<arr1.length && j<arr2.length){
        if (arr1[i]<arr2[j]){
            result.push(arr1[i]);
            i++;
        }else{
            result.push(arr2[j]);
            j++;
    }
    while (i<arr1.lenght)
            result.push(arr1[i]);
            i++
    while (i<arr2.lenght)
            result.push(arr2[j]);
        j++;
}
    return result;
}
console.log(merge([1,3,5],[2,4,6]));
