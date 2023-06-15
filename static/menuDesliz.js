document.addEventListener('keydown', function(event) {
if (event.key === 'ArrowUp' || event.key === 'ArrowDown') {
    cambiar(event.key);
}
});
//Inicializar variable para controlar el botón actual.
let idBoton = ['#iniciar','#memorama','#terminar'];
let idBValor = 0;

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

let botonActivo = idBoton[idBValor]

const btn = document.querySelector(botonActivo);
let nuevoContenido = btn.textContent;

// Función auxiliar para mostrar la secuencia de caracteres
function mostrarSecuencia(i) {
    if (i < nuevoContenido.length) {
    let j = 0;
    let secuencia = [">", "*", "<", "*"];
    let intervalo = setInterval(() => {
        btn.textContent = nuevoContenido.slice(0, i) + secuencia[j];
        j++;
        if (j === secuencia.length) {
        clearInterval(intervalo);
        btn.textContent = nuevoContenido.slice(0, i + 1);
        mostrarSecuencia(i + 1);
        }
    }, 40);
    }
}

// Llamar a la función auxiliar para el primer carácter
mostrarSecuencia(0);
};
