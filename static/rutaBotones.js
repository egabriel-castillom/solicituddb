function cambioMenu(nuevoContenido){
    let ocultarMenu = document.querySelector(".principal");
    ocultarMenu.style.display = "none";
    let mostrarMenu = document.querySelector(nuevoContenido);
    mostrarMenu.style.display = "grid";

}