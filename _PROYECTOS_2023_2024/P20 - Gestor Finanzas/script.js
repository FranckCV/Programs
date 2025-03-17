window.onload = function() {
    // Mostrar y ocultar menú de opciones al hacer clic en el icono de tres puntos
    document.addEventListener('click', function(event) {
        var optionsMenus = document.querySelectorAll('.options-menu');
        optionsMenus.forEach(function(menu) {
            menu.style.display = 'none';
        });

        if (event.target.classList.contains('options-icon')) {
            var optionsMenu = event.target.nextElementSibling;
            if (optionsMenu.style.display === 'block') {
                optionsMenu.style.display = 'none';
            } else {
                optionsMenu.style.display = 'block';
            }
        } else {
            optionsMenus.forEach(function(menu) {
                menu.style.display = 'none';
            });
        }
    });

    // Agregar nueva transacción
    var addButton = document.getElementById('addButton');
    addButton.addEventListener('click', function() {
        var modal = document.getElementById('transactionModal');
        var closeButton = document.querySelector('.close');
        var form = document.createElement('form');
        form.innerHTML = `
            <label for="amount">Monto:</label>
            <input type="number" id="amount" name="amount" pattern="[0-9.-]*" required><br>
            <label for="description">Descripción:</label>
            <input type="text" id="description" name="description" required><br>
            <label for="date">Fecha:</label>
            <input type="date" id="date" name="date" value="${getCurrentDate()}" required><br>
            <label for="time">Hora:</label>
            <input type="time" id="time" name="time" value="${getCurrentHour()}" required><br>
            <button type="submit">Guardar</button>
        `;
        modal.querySelector('.modal-content').appendChild(form);
        modal.style.display = 'block';

        // Cerrar el modal al hacer clic en el botón de cerrar
        closeButton.onclick = function() {
            modal.style.display = 'none';
            form.reset();                   
        };

        // Agregar la transacción a la lista al enviar el formulario
        form.addEventListener('submit', function(event) {
            event.preventDefault();
            var amount = this.querySelector('#amount').value;
            var description = this.querySelector('#description').value;
            var date = this.querySelector('#date').value;
            var time = this.querySelector('#time').value;
            var transactionsList = document.querySelector('.transactions-list');
            var transactionItem = document.createElement('li');
            transactionItem.classList.add('transaction');
            transactionItem.innerHTML = `
                <span>${amount}</span>
                <span>${description}</span>
                <span>${date}</span>
                <span>${time}</span>
                <span class="options-icon"><i class="fas fa-ellipsis-v"></i></span>
                <div class="options-menu">
                    <ul>
                        <li>Editar</li>
                        <li>Eliminar</li>

                        <div class="dropdown-item">
                            <span class="currentlink " role="menuitem">
                                <img class="icon " alt="" aria-hidden="true" src="https://intranet.usat.edu.pe/aulavirtual/theme/image.php/lambda/core/1675974088/i/navigationitem">
                                Editar
                            </span>
                        </div>

                        <div class="dropdown-item">
                            <span class="currentlink " role="menuitem">
                                <img class="icon " alt="" aria-hidden="true" src="https://intranet.usat.edu.pe/aulavirtual/theme/image.php/lambda/core/1675974088/i/navigationitem">
                                Eliminar
                            </span>
                        </div>


                    </ul>
                </div>                
            `;
            transactionsList.appendChild(transactionItem);
            modal.style.display = 'none';
            form.reset();
        });
    });

    var today = new Date();

    // Función para obtener la fecha actual en el formato yyyy-mm-dd
    function getCurrentDate() {        
        var dd = String(today.getDate()).padStart(2, '0');
        var mm = String(today.getMonth() + 1).padStart(2, '0'); // Enero es 0!
        var yyyy = today.getFullYear();
        return yyyy + '-' + mm + '-' + dd;
    }
    
    // Función para obtener la hora actual en el formato hh:mm:ss
    function getCurrentHour() {
        var currentHour = today.getHours();
        var currentMinute = today.getMinutes();
        var formattedHour = currentHour < 10 ? "0" + currentHour : currentHour;
        var formattedMinute = currentMinute < 10 ? "0" + currentMinute : currentMinute;
        return formattedHour + ":" + formattedMinute;
    }
};
