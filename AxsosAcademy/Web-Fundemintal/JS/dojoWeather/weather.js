//Alert
function loadingAlert() {
    alert("Loading weather report...");
}

//Dismiss
function acceptCookies() {
    var element = document.querySelector("#cookie-bar");
    element.remove();
}

//Temperature 
function cToF(temp) {
    return Math.round(9 / 5 * temp + 32);
}

function fToC(temp) {
    return Math.round(5 / 9 * (temp - 32));
}

function convert(element) {
    console.log(element.value);
    for (var i = 1; i < 9; i++) {
        var tempSpan = document.querySelector(".temps span:nth-child(" + i + ")");
    }
    var temps = document.querySelectorAll(".high, .low");
    for (var i = 0; i < temps.length; i++) {
        var currentTempValue = parseInt(temps[i].innerText);
        if (element.value == "f") {
            temps[i].innerText = cToF(currentTempValue);
        } else {
            temps[i].innerText = fToC(currentTempValue);
        }
    }
}