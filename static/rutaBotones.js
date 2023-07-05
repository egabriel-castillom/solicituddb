function cambioMenu(nuevoContenido,elemento){
    let elementoAnimado = document.getElementById(elemento);
    elementoAnimado.classList.add('aguaAnimacion');
    setTimeout( function() {
        elementoAnimado.classList.remove('aguaAnimacion');
        let ocultarMenu = document.querySelector(".principal");
        ocultarMenu.style.display = "none";
        let mostrarMenu = document.querySelector(nuevoContenido);
        mostrarMenu.style.display = "grid";        
    }, 1000);


}