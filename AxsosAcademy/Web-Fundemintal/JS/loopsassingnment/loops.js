for (var i = 1; i < 11; i++) {
    console.log(i);
}
// 
for (var i = 10; i > 0; i = i - 1) {
    console.log(i);
}
// 
for (var i = 1; i < 21; i++) {
    if (i % 2 == 0) {
        console.log(i);
    }
}
// 
for (var i = 1; i < 21; i++) {
    if (i % 2 != 0) {
        console.log(i);
    }
}
// 
var sum = 0;
for (var i = 1; i < 11; i++) {
    sum += i;
}
console.log(sum)
// 
for (var i = 1; i < 31; i++) {
    if (i % 3 == 0 && i % 5 == 0) {
        console.log(i,"FizzBuzz");
    }
    else if (i % 5 == 0) {
        console.log(i,"Buzz");
    } 
    else if(i % 3 == 0) {
        console.log(i,"Fizz");
    }
    else{
        console.log(i);
    }
}