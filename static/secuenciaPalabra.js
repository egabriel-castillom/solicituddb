// Función auxiliar para mostrar la secuencia de caracteres
function mostrarSecuencia(i,btn,nuevoContenido,idBValor) {
    //Un nuevo elemento(idBValor) es seleccionado para mostrar una secuencia.
    let llamada = 1;
    if (idBValor === 0){
        sessionStorage.setItem('llamada0',JSON.stringify(llamada));
    };
    if (idBValor === 1){
        sessionStorage.setItem('llamada1',JSON.stringify(llamada));
    };
    if (idBValor === 2){
        sessionStorage.setItem('llamada2',JSON.stringify(llamada));
    };
    if (i < nuevoContenido.length) {
    let j = 0;
    let secuencia = [">", "*", "<", "*"];
    let intervalo = setInterval(() => {
        btn.textContent = nuevoContenido.slice(0, i) + secuencia[j];
        j++;
        if (j === secuencia.length) {
        clearInterval(intervalo);
        btn.textContent = nuevoContenido.slice(0, i + 1);
        mostrarSecuencia(i + 1,btn,nuevoContenido,idBValor);
        }
    }, 40);
    }else{
        llamada = 0;
        if (idBValor === 0){
            sessionStorage.setItem('llamada0',JSON.stringify(llamada));
        };
        if (idBValor === 1){
            sessionStorage.setItem('llamada1',JSON.stringify(llamada));
        };
        if (idBValor === 2){
            sessionStorage.setItem('llamada2',JSON.stringify(llamada));
        };
    }
};
