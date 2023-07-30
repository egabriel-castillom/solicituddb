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

//Si se detecta algún swipe en panatalla, se llama a la
//función cambiar
document.addEventListener('touchstart', handleTouchStart, false);        
document.addEventListener('touchmove', handleTouchMove, false);

var yDown = null;                                                        

function handleTouchStart(evt) {                                         
    yDown = evt.touches[0].clientY;                                      
};                                                

function handleTouchMove(evt) {
    if ( ! yDown ) {
        return;
    }

    var yUp = evt.touches[0].clientY;
    var yDiff = yDown - yUp;

    if (sessionStorage.getItem('running') !== 'yes'){
        if ( yDiff > 0 ) {
            /* down swipe */ 
            cambiar('ArrowDown');
        } else { 
            /* up swipe */
            cambiar('ArrowUp');
        }
        sessionStorage.setItem('running','yes');
    }                                                                 
    /* reset values */
    yDown = null;                                             
};

//Si se detecta algún scroll en el, se llama a la
//función cambiar
document.addEventListener('wheel', handleWheel, false);

function handleWheel(evt) {
    if (sessionStorage.getItem('running') !== 'yes'){
        if (evt.deltaY < 0) {
            /* scroll up */
            cambiar('ArrowUp');
        } else {
            /* scroll down */
            cambiar('ArrowDown');
        }
        sessionStorage.setItem('running','yes');
    }
};
//Inicializar variable para controlar el botón actual.
let idBoton = ['#sobreMi','#portafolio','#contacto'];
let idBValor = 0;
let llamada = 0;
sessionStorage.setItem('llamada0',JSON.stringify(llamada))
sessionStorage.setItem('llamada1',JSON.stringify(llamada))
sessionStorage.setItem('llamada2',JSON.stringify(llamada))
//Funcion para cambiar el elemento visible en el menu incial
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
//if (JSON.parse(sessionStorage.getItem('llamada'+idBValor.toString())) !== 1){
//    let botonActivo = idBoton[idBValor]
//    const btn = document.querySelector(botonActivo);
//    let nuevoContenido = btn.textContent;
//    setTimeout (function () {
//        mostrarSecuencia(0,btn,nuevoContenido,idBValor);
//    },200);

//};

//Llamar a la función que muestra el botón siguiente según el desplazamiento del menu.
let idBotonSinHash = idBoton.map(function(id){ return id.slice(1)});   
let idSeleccion = idBotonSinHash[idBValor];
let seleccion = document.getElementById(idSeleccion);
let todosBotones = document.querySelectorAll('button');
    if(direccion === 'ArrowDown'){
        animacionAbajo(todosBotones,idSeleccion,seleccion)
    } else{
        animacionArriba(todosBotones,idSeleccion,seleccion);
    };
};
