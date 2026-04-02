// display odd no. from 1 - 20 //
for (let i = 1; i <= 20; i++) {
    if (i % 2 !== 0) 
        console.log(i);
}

// decrease multiples 0f 3 //
for (let i = 100; i >= 0; i--) {
    if (i % 3 === 0)
        console.log(i);
}

// print the given sequence 4, 2.5, 1, -0.5, -2, -3.5 //
for (let i = 4; i >= -3.5; i -= 1.5) {
    console.log(i);
}

// sigma (sum from 1 - 100) //
let sum = 0;
for (let i = 1; i <= 100; i++) {
    sum += i;
    console.log(sum);
}

// factorial 1 - 12 //
let result = 1;
for (let i = 1; i <= 12; i++) {
    result *= i;
    console.log(result);
}