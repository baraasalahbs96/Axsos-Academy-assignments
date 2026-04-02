
function changeName() {
    var userName = document.querySelector("#user-name");
    userName.innerText = "Baraa Salah";
}

var connectionRequests = document.querySelector("#connection-requests");
var yourConnections = document.querySelector("#your-connections");

function accept(id) {
    reject(id);
    yourConnections.innerText++;
}

function reject(id) {
    var elem = document.querySelector("#" + id);
    elem.remove();
    connectionRequests.innerText--;
}