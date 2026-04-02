// Print Numbers
// Write a for loop to print numbers from 1 to 10.
for (let i=1; i<=10; i++){
    console.log(i);
}

// Reverse Counting
// Write a for loop to print numbers from 10 to 1.
for (let i=10; i>=1; i--){
    console.log(i);
}

// Even Numbers
// Write a for loop to print all even numbers between 1 and 20.
for (let i=2; i<=20; i+=2){
    console.log(i);
}

// Odd Numbers
// Write a for loop to print all odd numbers between 1 and 20.
for (let i=1; i<=20; i+=2){
    console.log(i);
}

// Sum of Numbers
// Write a for loop to calculate and print the sum of numbers from 1 to 10.
let sum=0;
for (i=1; i<=10; i++){
    sum+=i;
} console.log("sum",sum);
// FizzBuzz
// Write a for loop to print numbers from 1 to 30.
// If the number is divisible by 3, print "Fizz".
// If divisible by 5, print "Buzz".
// If divisible by both 3 and 5, print "FizzBuzz".
for (let i=1; i<=30; i++){
    if (i%3==0 && i%5==0){
        console.log("FizzBuzz");
    } else if (i%3==0){
        console.log("Fizz");
    } else if (i%5==0){
        console.log("Buzz");
    }else{
        console.log(i);
    }
} 
