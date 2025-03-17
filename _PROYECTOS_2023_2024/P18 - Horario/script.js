window.onload = function() {
    var scheduleTable = document.getElementById("schedule");
    var rows = 24; // Número de filas
    var cols = 7; // Número de columnas

    // Generar filas y columnas
    for (var i = 0; i < rows; i++) {
        var row = scheduleTable.insertRow();
        for (var j = 0; j < cols; j++) {
            var cell = row.insertCell();
            cell.dataset.row = i;
            cell.dataset.col = j;
            cell.addEventListener("click", function() {
                selectCell(this);
            });
        }
    }

    // Función para seleccionar celda
    function selectCell(cell) {
        // Desmarcar celda anteriormente seleccionada
        var selectedCell = document.querySelector(".selected");
        if (selectedCell) {
            selectedCell.classList.remove("selected");
        }
        // Marcar celda seleccionada
        cell.classList.add("selected");
    }
};
