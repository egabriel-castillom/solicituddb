//Si se detecta algún a flecha en el teclado, se llama a la
//función cambiar
sessionStorage.setItem('running','no');
document.addEventListener('keydown', function(event) {
if (event.key === 'ArrowUp' || event.key === 'ArrowDown') {
    if (sessionStorage.getItem('running') !== 'yes'){
        cambiar(event.key);
        sessionStorage.setItem('running','yes');
    }

}
});

//Inicializar variable para controlar el botón actual.
let idBoton = ['#sobreMi','#portafolio','#contacto'];
let idBValor = 0;
let llamada = 0;
sessionStorage.setItem('llamada0',JSON.stringify(llamada))
sessionStorage.setItem('llamada1',JSON.stringify(llamada))
sessionStorage.setItem('llamada2',JSON.stringify(llamada))

//Funcion inicial para ejecutar secuencia a lo largo de 
//el texto contenedor del botón
function cambiar(direccion) {
if (direccion ==='ArrowUp'){
    idBValor = idBValor - 1;
}else{
    idBValor = idBValor + 1;
};
if (idBValor < 0){
    idBValor = 2;
};
if (idBValor > 2){
    idBValor = 0;
};

//Se comprueba si es que el boton seleccionado se encuentra ejecutando
//una secuencia, de ser así no se permite interrumpirla
if (JSON.parse(sessionStorage.getItem('llamada'+idBValor.toString())) !== 1){
    let botonActivo = idBoton[idBValor]
    const btn = document.querySelector(botonActivo);
    let nuevoContenido = btn.textContent;


    //Llamar a la función de secuencia para el boton seleccionado
    if (JSON.parse(sessionStorage.getItem('llamada0')) === 0 || JSON.parse(sessionStorage.getItem('llamada1')) === 0 || JSON.parse(sessionStorage.getItem('llamada2')) === 0){
        mostrarSecuencia(0,btn,nuevoContenido,idBValor);
    };
}

//Llamar a la función que muestra el botón seleccionado
mostrarSeleccion(idBValor, idBoton, direccion);
};
