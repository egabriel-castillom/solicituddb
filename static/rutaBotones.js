function mostrarOcultarElemento(elemento,accion){
    let elementoUsado = document.querySelector(elemento);
    if (accion=='mostrar'){
        elementoUsado.style.display = "flex";
    } else{
        elementoUsado.style.display = "none";
    };
}

//onclick="mostrarOcultarElemento('.mypopupframe','mostrar')"
//onclick="mostrarOcultarElemento('.mypopupframe','ocultar')"
//display: none;
//position: absolute;
//top: 0;
//left: 0;
//z-index: 1;
