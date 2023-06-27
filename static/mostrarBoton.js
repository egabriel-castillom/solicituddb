function mostrarSeleccion(idBValor, idBoton, direccion){ 	
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