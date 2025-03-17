const tablasCalificacion = document.querySelectorAll(".table_element");
tablasCalificacion.forEach(tablaCalificacion => {
    const resultadoFinal = tablaCalificacion.querySelector("#resultado");

    function calcularNotas() {
        let promedioGeneral = 0;
        let sumaPesosUnidades = 0;

        const unidades = [...new Set(Array.from(tablaCalificacion.querySelectorAll("tr[data-unidad]"))
            .map(tr => tr.dataset.unidad))];

        unidades.forEach(unidadId => {
            const unidadFila = tablaCalificacion.querySelector(`tr[data-unidad="${unidadId}"]:not(.seccion_nota)`);
            const filasNotas = tablaCalificacion.querySelectorAll(`tr[data-unidad="${unidadId}"].seccion_nota`);

            if (!unidadFila || filasNotas.length === 0) return;

            const subtotalDiv = unidadFila.querySelector(".subtotal");
            const porcentajeUnidad = parseFloat(unidadFila.querySelector("p").textContent.replace("%", "")) / 100;
            let subtotalUnidad = 0;

            filasNotas.forEach(notaFila => {
                const inputNota = notaFila.querySelector("input[type='number']");
                const porcentajeNotaElem = notaFila.querySelector("p");

                if (!inputNota || !porcentajeNotaElem) return;

                const porcentajeNota = parseFloat(porcentajeNotaElem.textContent.replace("%", "")) / 100;
                const nota = parseFloat(inputNota.value) || 0;

                var valor = inputNota.value;
                if (valor > 20) {
                    inputNota.value = 20;
                } else {
                    if (13.5 > valor) {
                        inputNota.style.color = "red";
                    } else if (13.5 == valor) {
                        inputNota.style.color = "yellow";
                    }  else {
                        inputNota.style.color = "white";
                    }
                }

                subtotalUnidad += nota * porcentajeNota;
            });

            subtotalDiv.textContent = subtotalUnidad.toFixed(2);

            promedioGeneral += subtotalUnidad * porcentajeUnidad;
            sumaPesosUnidades += porcentajeUnidad;
        });

        resultadoFinal.textContent = sumaPesosUnidades > 0 ? (promedioGeneral / sumaPesosUnidades).toFixed(2) : "00.00";
    }

    tablaCalificacion.querySelectorAll("input[type='number']").forEach(input => {
        input.addEventListener("input", () => {
            calcularNotas();
        });
    });

    calcularNotas();
}

);
