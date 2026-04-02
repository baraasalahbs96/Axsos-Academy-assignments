// variables
let displayVariable = document.querySelector("display");
let firstNumber ="";
let operator ="";
// Press()
function press(value){
    if (displayVariable.textContent== "0"){
        displayVariable.textContent= value;
    }else {
        displayVariable.textContent+= value;
    }
}
// setOp()
function setOp(op) {
    firstNumber= displayVariable.textContent;
    operator= op;
    displayVariable.textContent= "0";
}
// calcullate()
function calculate(){
    let secondNumber= displayVariable.textContent;
    let result= 0;
    if (operator=="+"){
        result= parseFloat(firstNumber) + parseFloat(secondNumber);
    }else if (operator== "-"){
        result= parseFloat(firstNumber) - parseFloat(secondNumber);
    }else if (operator== "*"){
        result= parseFloat(firstNumber) * parseFloat(secondNumber);
    }else if (operator== "/"){
        result= parseFloat(firstNumber) / parseFloat(secondNumber);
    }
    displayVariable.textContent= result;
}
 // clr()
function clr(){
    displayVariable.textContent= "0";
    firstNumber="";
    operator="";
}