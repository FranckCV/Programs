const canvas = document.getElementById('diagramCanvas');
const ctx = canvas.getContext('2d');
const entities = []; // Almacena las entidades
let selectedEntity = null;

// Función para dibujar entidades
function drawEntities() {
    ctx.clearRect(0, 0, canvas.width, canvas.height); // Limpia el canvas
    entities.forEach((entity) => {
        ctx.fillStyle = 'lightblue';
        ctx.fillRect(entity.x, entity.y, 150, 50);
        ctx.strokeStyle = 'black';
        ctx.strokeRect(entity.x, entity.y, 150, 50);
        ctx.fillStyle = 'black';
        ctx.fillText(entity.name, entity.x + 20, entity.y + 30);
    });
}

// Añadir nueva entidad al hacer clic en el botón
document.getElementById('addEntity').addEventListener('click', () => {
    const newEntity = {
        x: 50, // Posición inicial por defecto
        y: 50,
        name: `Entidad ${entities.length + 1}`,
    };
    entities.push(newEntity);
    drawEntities();
});

let offsetX, offsetY;

// Detectar clic para mover entidades
canvas.addEventListener('mousedown', (e) => {
    const mouseX = e.offsetX;
    const mouseY = e.offsetY;

    // Buscar si se clicó sobre alguna entidad
    selectedEntity = entities.find((entity) =>
        mouseX > entity.x &&
        mouseX < entity.x + 150 &&
        mouseY > entity.y &&
        mouseY < entity.y + 50
    );

    if (selectedEntity) {
        offsetX = mouseX - selectedEntity.x;
        offsetY = mouseY - selectedEntity.y;
    }
});

// Mover entidad seleccionada
canvas.addEventListener('mousemove', (e) => {
    if (selectedEntity) {
        selectedEntity.x = e.offsetX - offsetX;
        selectedEntity.y = e.offsetY - offsetY;
        drawEntities();
    }
    // ctx.strokeStyle = selectedEntity === entity ? 'red' : 'black';
});

// Soltar entidad
canvas.addEventListener('mouseup', () => {
    selectedEntity = null;
});










// // const canvas = document.getElementById('canvas');
// // const ctx = canvas.getContext('2d');

// // // Ajustar tamaño dinámico del lienzo
// // canvas.width = canvas.offsetWidth;
// // canvas.height = canvas.offsetHeight;

// // // Dibujar una tabla (placeholder)
// // ctx.fillStyle = '#4CAF50';
// // ctx.fillRect(100, 100, 150, 80);
// // ctx.fillStyle = '#fff';
// // ctx.font = '16px Arial';
// // ctx.fillText('Tabla: Usuarios', 110, 140);



// const canvas = document.getElementById('diagramCanvas');
// const ctx = canvas.getContext('2d');

// // Dibuja una entidad
// ctx.fillStyle = 'lightblue';
// ctx.fillRect(50, 50, 150, 50);
// ctx.strokeStyle = 'black';
// ctx.strokeRect(50, 50, 150, 50);
// ctx.fillStyle = 'black';
// ctx.fillText('Entidad 1', 75, 75);

// // Conexión
// ctx.beginPath();
// ctx.moveTo(200, 75); // Punto inicial
// ctx.lineTo(300, 75); // Punto final
// ctx.stroke();

// // Otra entidad
// ctx.fillStyle = 'lightgreen';
// ctx.fillRect(300, 50, 150, 50);
// ctx.strokeStyle = 'black';
// ctx.strokeRect(300, 50, 150, 50);
// ctx.fillStyle = 'black';
// ctx.fillText('Entidad 2', 325, 75);




// canvas.addEventListener('click', function (event) {
//     const x = event.offsetX;
//     const y = event.offsetY;

//     // Crea una nueva entidad en el punto del clic
//     ctx.fillStyle = 'lightyellow';
//     ctx.fillRect(x, y, 150, 50);
//     ctx.strokeStyle = 'black';
//     ctx.strokeRect(x, y, 150, 50);
//     ctx.fillStyle = 'black';
//     ctx.fillText('Nueva Entidad', x + 20, y + 30);
// });



// const diagramData = [];
// function addEntity(x, y, name) {
//     diagramData.push({ x, y, name });
// }

// // Al hacer clic:
// canvas.addEventListener('click', function (event) {
//     const x = event.offsetX;
//     const y = event.offsetY;
//     addEntity(x, y, 'Nueva Entidad');
// });

// // Botón para exportar
// document.getElementById('export').addEventListener('click', () => {
//     console.log(JSON.stringify(diagramData));
// });

// document.getElementById('saveAsImage').addEventListener('click', () => {
//     const link = document.createElement('a');
//     link.download = 'diagram.png';
//     link.href = canvas.toDataURL();
//     link.click();
// });
