// Write a program that checks if a number is positive or negative.
var number= 0;
if(number>=0) {
    console.log("positive");
} else if(number<0) {
    console.log("negative");
}


// Write a program that prints "Good morning" if the time is less than 12 and "Good afternoon" otherwise.
var time= 10;
if(time<12) {
    console.log("good morning");
} else {
    console.log("good afternoon");
}

// Write a program that assigns grades based on scores:

// 90 and above: A
// 80–89: B
// 70–79: C
// Below 70: F
var grades="";
switch(grades){
    case "90 and above":
        console.log("A");
    break;
    case "80-89":
        console.log("B");
        break;
    case "70-79":
        console.log("C");
        break;
    case "Below 70":
        console.log("F");
        break;
        default:
        console.log("not qualified");

}

// Write a program that takes a day of the week and prints whether it’s a weekday or weekend.
var day="";
switch(day){
    case "saturday":
        console.log("it’s a weekend");
        break;
    case"sunday":
        console.log("it’s a weekend");
        break;
    case "Monday":
        console.log("it’s a weekday");
        break;
    case "Tuesday":
        console.log("it’s a weekday");
        break;
    case ("wednesday"):
        console.log("it’s a weekday");
        break;
    case ("thursday"):
        console.log("it’s a weekday");
        break;
    case ("Friday"):
        console.log("it’s a weekday");
        break;
        default:
}

