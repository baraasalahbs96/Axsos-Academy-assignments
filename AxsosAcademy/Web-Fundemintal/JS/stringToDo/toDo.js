function removeBlanks(str) {
    var output = "";
    for (var i = 0; i < str.length; i++) {
        if (str[i] !== " ") {
            output += str[i];
        }
    }
    return output;
}
console.log(removeBlanks("b    a    r    a     a"))

// 
function getDigits(str) {
    var output = "";
    for (var i = 0; i < str.length; i++) {
        if (!isNaN(str[i])) {
            output += str[i];
        }
    }
    return output;
}
console.log(getDigits("b96ar9a6a"))

// 
function getAcronyms(str) {
    var words = str.split(" ");
    var output = "";
    for (var i = 0; i < words.length; i++) {
        var word = words[i];
        if (word !== "") {
            output += word[0].toUpperCase();
        }
    }
    return output;
}
console.log(getAcronyms(" there's no free lunch - gotta pay yer way. "))

// 
function countNotSpaces(str) {
    var count = 0;
    for (var i = 0; i < str.length; i++) {
        if (str[i] !== " ") {
            count++;
        }
    }
    return count;
}
console.log(countNotSpaces("b    a    r    a     a"))

// 

function removeShorterString(arr, minLength) {
    var output = [];
    for (var i = 0; i < arr.length; i++) {
        if (arr[i].length >= minLength) {
            output[output.length] = arr[i];
        }
    }
    return output;
}
var removedShorter = removeShorterString(['hello', 'snowy', 'the', 'world', 'says', 'hello', 'ba'], 6);
console.log(removedShorter)