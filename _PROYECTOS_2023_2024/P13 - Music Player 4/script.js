document.addEventListener('DOMContentLoaded', function () {
    const audioPlayer = document.getElementById('audioPlayer');
    const playlist = document.getElementById('playlist');
    const fileInput = document.getElementById('fileInput');
    const player = document.getElementById('player');
    let currentSongIndex = 0;
    let songs = [];

    // Cargar lista de reproducción desde almacenamiento local
    if (localStorage.getItem('playlist')) {
        songs = JSON.parse(localStorage.getItem('playlist'));
        loadPlaylist();
    }

    function loadPlaylist() {
        playlist.innerHTML = '';
        songs.forEach((song, index) => {
            const li = document.createElement('li');
            li.textContent = song.name;
            li.draggable = true;
            li.addEventListener('click', () => playSong(index));
            li.addEventListener('contextmenu', (e) => {
                e.preventDefault();
                showContextMenu(e.clientX, e.clientY, index);
            });
            li.addEventListener('dragstart', (e) => {
                e.dataTransfer.setData('text/plain', index);
            });
            playlist.appendChild(li);
        });
        // Guardar la lista de reproducción en almacenamiento local
        localStorage.setItem('playlist', JSON.stringify(songs));
    }

    function playSong(index) {
        currentSongIndex = index;
        const song = songs[index];
        audioPlayer.src = URL.createObjectURL(song);
        audioPlayer.play();
    }

    function showContextMenu(x, y, index) {
        // Mostrar menú contextual
    }

    function allowDrop(ev) {
        ev.preventDefault();
    }

    function drop(ev) {
        ev.preventDefault();
        const fromIndex = parseInt(ev.dataTransfer.getData('text/plain'));
        const toIndex = Array.from(playlist.children).indexOf(ev.target);
        if (isNaN(toIndex)) return;
        const [removed] = songs.splice(fromIndex, 1);
        songs.splice(toIndex, 0, removed);
        loadPlaylist();
    }

    fileInput.addEventListener('change', () => {
        songs = [];
        for (const file of fileInput.files) {
            songs.push(file);
        }
        loadPlaylist();
    });

    document.getElementById('playPauseButton').addEventListener('click', () => {
        if (audioPlayer.paused) {
            audioPlayer.play();
            document.getElementById('playPauseButton').innerHTML = '<i class="fa fa-pause"></i>';
        } else {
            audioPlayer.pause();
            document.getElementById('playPauseButton').innerHTML = '<i class="fa fa-play"></i>';
        }
    });

    document.getElementById('stopButton').addEventListener('click', () => {
        audioPlayer.pause();
        audioPlayer.currentTime = 0;
        document.getElementById('playPauseButton').innerHTML = '<i class="fa fa-play"></i>';
    });

    document.getElementById('prevButton').addEventListener('click', () => {
        currentSongIndex = (currentSongIndex - 1 + songs.length) % songs.length;
        playSong(currentSongIndex);
    });

    document.getElementById('nextButton').addEventListener('click', () => {
        currentSongIndex = (currentSongIndex + 1) % songs.length;
        playSong(currentSongIndex);
    });

    document.addEventListener('contextmenu', () => {
        // Ocultar menú contextual
    });

    // Mover el reproductor por la página
    let isDragging = false;
    let offset = { x: 0, y: 0 };

    player.addEventListener('mousedown', (e) => {
        isDragging = true;
        offset.x = player.offsetLeft - e.clientX;
        offset.y = player.offsetTop - e.clientY;
    });

    document.addEventListener('mousemove', (e) => {
        if (isDragging) {
            player.style.left = (e.clientX + offset.x) + 'px';
            player.style.top = (e.clientY + offset.y) + 'px';
        }
    });

    document.addEventListener('mouseup', () => {
        isDragging = false;
    });
});