const audio = document.getElementById("audio");
const playPause = document.getElementById("play");

playPause.addEventListener("click", () => {
    if (audio.paused || audio.ended) {
        playPause.querySelector(".pause-btn").classList.toggle("hide");
        playPause.querySelector(".play-btn").classList.toggle("hide");
        audio.play();
    } else {
        audio.pause();
        playPause.querySelector(".pause-btn").classList.toggle("hide");
        playPause.querySelector(".play-btn").classList.toggle("hide");
    }
});

var reproductor = document.getElementById("audio");

barra.addEventListener("change", function (ev) {
    reproductor.volume = ev.currentTarget.value;
}, true);









