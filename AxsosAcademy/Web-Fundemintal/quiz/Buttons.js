let starBtn = document.getElementById("starBtn");
starBtn.onmouseover = function() {
    document.body.style.backgroundColor = "yellow";
}
starBtn.onmouseout = function() {
    document.body.style.backgroundColor = "white";
}

//

let changeBtn = document.getElementById("changeBtn");
let title = document.getElementById("whoTitle");
let text = document.getElementById("whoText");
let image = document.getElementById("whoImg");
let isChanged = false;

changeBtn.onclick = function() {
    if (!isChanged) {
        title.innerText = "Our mission";
        text.innerText = "Our mission is to empower businesses with cutting-edge digital solutions that drive growth and success.";
        image.src = "Screenshot 2026-04-03 at 11.21.25 AM.png";
        isChanged = true;
    }
else {
        title.innerText = "Who we are";
        text.innerText = "We are forward-thinking company dedicated to providing innovative solutions that fuel business growth. with a focus on modern technologies and strategic insights, we help businesses streamline their operations, ennhance customer experiences, and drive sustainable growth.";
        image.src = "Screenshot 2026-04-03 at 11.21.25 AM.png";
        isChanged = false;
    }
}
    // 
let addService = document.getElementById("addService");
let servicesCard = document.getElementById("servicesCard");
addService.onclick = function() {
    let newCard = document.createElement("div");
    newCard.className = "card";
    newCard.innerHTML = `
    <div class="card">
        <img src="Screenshot 2026-04-03 at 11.21.25 AM.png" alt="Service Image">
        <p>we provide comprehensive consulting services to help you navigate the complexities of business growth.</p>
    </div>
    `;
    servicesCard.appendChild(newCard);
}