// reverse string
function reverseString(str){
    let reversed="";
    for(let i = str.length - 1; i >= 0; i--){
        reversed +=str[i];
    }
    return reversed;
}
console.log(reversedString("hello"));

// vowels

function countVowels(str){
    let count="";
    for(char of str){
        if(vowels.includes(char))
            count++;
    }
    returncount;
}
console.log(countvowels("Baraa"));

// Palindrome

function isPalendrome(str){
    let reversedStr="";
    for (let i = str.length - 1; i >= 0; i--){
        reversedStr += str[i];
    }
    if(str === reversedStr){
        return true;
    } else{
        return false;
    }
}
console.log(isPalindrome("dad"));


// longest word

function longestWord(str){
    let longest="";
    for(let longest of longestWord){
        if(longestWord.length > longest.length)
            longest= longestWord
    }
    return longest;
}
console.log(longestWord("i love solving algorithms"));

// grades // switch

function feedBack(grade){
    let result;
    switch (grade){
        case 'A':
            result = "Excellent";
            break
        case 'B':
            result = "Good job";
            break
        case 'C':
            result = "You passed";
            break
        case 'D':
            result = "Need improvement";
            break
        case 'F':
            result = "Failed";
            break
        default:
            result = "Invalid grade";
    }
    return result;
}
console.log(feedBack("B"));

// count char // switch

function countChar(str){
    let vowels = "";
    let digits = "";
    let spaces = "";
    let others = "";
        for (let i = 0; i < str.length; i++){
            let char = str[i];
            switch (char){
                case 'a': case 'e': case 'i': case 'o': case 'u':
                case 'A': case 'E': case 'I': case 'O': case 'U':
                    vowels++;
                    break;
                case ' ':
                    spaces++;
                    break;
                default:
                    if (char >= '0' && char <= '9'){
                        digits++;
                    } else {
                        others++;
                    }
            }
        }
        return{
            vowels: vowels,
            digits: digits,
            spaces: spaces,
            others: others
        };
}
console.log(countChar("hi 123!"));
