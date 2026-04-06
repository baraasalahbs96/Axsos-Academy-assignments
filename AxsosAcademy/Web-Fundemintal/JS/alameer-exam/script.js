function removeBtn(btn){
    btn.remove();
}

let changeBtn = document.getElementById("changeBtn");
let image = document.getElementById("whoImg");
let isChanged = false;
changeBtn.onclick = function() {
    if (!isChanged) {
        image.src = "blue-super-car.png";
        isChanged = true;
    }
}
var count = 3;
function addLike() {
    var likesCount = document.querySelector("#likes");
    count--; //count=count-1
    likesCount.innerText = count;
}


let clientBtn = document.getElementById("clientBtn");
let clientImg =  document.getElementById("clientImg");
let clientPara =  document.getElementById("clientPara");
let changed = false;
clientBtn.onclick = function() {
     if (!isChanged) {
        clientImg.src = "client.png";
        clientPara.innerText = "I had a great experience at the car wash. The service was quick and effecient and my car was cleaned throughly with attention to detail. The staff were proffessional and committed toproviding the best service possible. Additionally, the prices wewe reasonable considering the quality of the work. I will deinitly be coming back and would recommend this car wash to anyone looking for excellent service.";
        changed = true;
    }
}
