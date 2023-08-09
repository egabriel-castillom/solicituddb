function mostrarOcultarElemento(elemento,accion){
    let elementoUsado = document.querySelector(elemento);
    if (accion=='mostrar'){
        elementoUsado.classList.add('aparecer'); // Agregamos la clase .aparecer al elemento
        setTimeout(() => { // Esperamos a que termine la animación antes de ocultar el elemento
            elementoUsado.classList.remove('aparecer'); // Removemos la clase .aparecer del elemento
        }, 500);
        elementoUsado.style.display = "flex";
    } else{
        elementoUsado.classList.add('desaparecer'); // Agregamos la clase .desaparecer al elemento
        setTimeout(() => { // Esperamos a que termine la animación antes de ocultar el elemento
            elementoUsado.style.display = "none";
            elementoUsado.classList.remove('desaparecer'); // Removemos la clase .desaparecer del elemento
        }, 500);        
    };
}

//onclick="mostrarOcultarElemento('.mypopupframe','mostrar')"
//onclick="mostrarOcultarElemento('.mypopupframe','ocultar')"
//display: none;
//position: absolute;
//top: 0;
//left: 0;
//z-index: 1;
