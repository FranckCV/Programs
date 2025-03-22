const activities = [
    { name: "IA", day: 2, hr_ini: 9, hr_fin: 14 },
    { name: "FyC", day: 2, hr_ini: 16, hr_fin: 19 },
    { name: "DAE", day: 2, hr_ini: 20, hr_fin: 22 },
    { name: "DAE", day: 4, hr_ini: 15, hr_fin: 19 },
    { name: "DAW", day: 3, hr_ini: 18, hr_fin: 21 },
    { name: "DAW", day: 5, hr_ini: 18, hr_fin: 21 },
    { name: "IO", day: 3, hr_ini: 15, hr_fin: 18 },
    { name: "IO", day: 5, hr_ini: 13, hr_fin: 15 },
    { name: "SO", day: 5, hr_ini: 15, hr_fin: 18 },
    { name: "SO", day: 4, hr_ini: 13, hr_fin: 15 },
];

const cols = 8, rows = 25, sizeCell = 50, sizeCol = 100, sizeRow = 30;
const grid = [];
const time = new Date();
const dayActual = time.getDay();
const horaActual = time.getHours();

function createGrid() {
    const gridElement = document.getElementById('grid');
    gridElement.style.gridTemplateColumns = `repeat(${cols}, ${sizeCol}px)`;
    gridElement.style.gridTemplateRows = `repeat(${rows + 1}, ${sizeRow}px)`;

    for (let i = 0; i < rows; i++) {
        grid[i] = [];
        for (let j = 0; j < cols; j++) {
            const cellElement = document.createElement('div');
            cellElement.classList.add('cell');
            gridElement.appendChild(cellElement);

            const cell = {
                x: i,
                y: j,
                isFill: false,
                parent: null,
                element: cellElement,
            };
            grid[i][j] = cell;

            if (i === 0) {
                cellElement.classList.add('cell_1');
            } else if (j === 0) {
                cellElement.classList.add('cell_2');
            } else {
                cellElement.setAttribute(`data-hrs`, `${i - 1}`);
                cellElement.setAttribute(`data-day`, `${j - 1}`);
            }

            if (i !== 0 && j === 0) {
                cellElement.innerHTML = `<span>${i - 1}:00</span>`;
            } else {
                for (const act of activities) {
                    if (parseInt(dayActual) + 1 > parseInt(cellElement.getAttribute("data-day"))) {
                        if (parseInt(dayActual) <= parseInt(cellElement.getAttribute("data-day"))) {
                            if (parseInt(cellElement.getAttribute("data-hrs")) < parseInt(horaActual)) {
                                cellElement.innerHTML = ``;
                                cellElement.classList.add(`pasado`);
                            } else if (
                                parseInt(cellElement.getAttribute("data-day")) === parseInt(act.day) &&
                                parseInt(cellElement.getAttribute("data-hrs")) >= parseInt(act.hr_ini) &&
                                parseInt(cellElement.getAttribute("data-hrs")) < parseInt(act.hr_fin)
                            ) {
                                cellElement.classList.add(`presente`);
                                cellElement.innerHTML = `<span>${act.name}</span>`;
                            }
                        } else {
                            cellElement.innerHTML = ``;
                            cellElement.classList.add(`pasado`);
                        }
                    } else if (
                        parseInt(cellElement.getAttribute("data-day")) === parseInt(act.day) &&
                        parseInt(cellElement.getAttribute("data-hrs")) >= parseInt(act.hr_ini) &&
                        parseInt(cellElement.getAttribute("data-hrs")) < parseInt(act.hr_fin)
                    ) {
                        cellElement.classList.add(`presente`);
                        cellElement.innerHTML = `<span>${act.name}</span>`;
                    }
                }
            }
        }
    }
}

createGrid();