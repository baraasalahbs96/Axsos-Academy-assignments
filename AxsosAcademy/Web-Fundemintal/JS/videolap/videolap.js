let video = document.getElementById("blossomVideo");
// onmiuseover
video.onmouseover = function() {
    video.play();
};
// onmouseout
video.onmouseout = function() {
    video.pause();
    video.currentTime = 0;
};