function animacionAbajo(todosBotones,idSeleccion,seleccion) {
    for (let i = 0; i<todosBotones.length; i++){
        if (todosBotones[i].style.display === 'inline' ){
            //APLICAR ANIMACIÓN A ELEMENTO POSTERIOR
                //Si el elemento seleccionado necesita un ajuste en animación.
            if (idSeleccion !== 'sobreMi'){
                seleccion.classList.add('animacionAbajoA');
            }else{
                seleccion.classList.add('animacionAbajo');
            };
            seleccion.style.display = 'inline';           
            todosBotones[i].classList.add('animacionArriba');
            setTimeout(function() {
                if (todosBotones[i] !== seleccion){
                    todosBotones[i].style.display = 'none';    
                }; 
                todosBotones[i].classList.remove('animacionArriba');        
                if (idSeleccion !== 'sobreMi'){
                    seleccion.classList.remove('animacionAbajoA');
                }else{
                    seleccion.classList.remove('animacionAbajo');
                };
                sessionStorage.setItem('running','no');
            }, 900);
        };
    };
};

function animacionArriba(todosBotones,idSeleccion,seleccion) {
    for (let i = 0; i<todosBotones.length; i++){
        if (todosBotones[i].style.display === 'inline' ){
            //Si el elemento seleccionado coincide con el elemento actual
            if (todosBotones[i] !== seleccion){
                console.log(todosBotones[i].className);
                console.log(seleccion.className);                
                if(todosBotones[i].className !== 'sobreMi'){
                    todosBotones[i].classList.add('animacionAbajoAR');                    
                }else{
                    todosBotones[i].classList.add('animacionAbajoR');                    
                };

            };
            //APLICAR ANIMACIÓN A ELEMENTO POSTERIOR
            seleccion.classList.add('animacionArribaR');
            seleccion.style.display = 'inline';
            setTimeout(function() {
                if (todosBotones[i] !== seleccion){
                    todosBotones[i].style.display = 'none';    
                }; 
                if(todosBotones[i].className !== 'sobreMi'){
                    todosBotones[i].classList.remove('animacionAbajoAR');                  
                }else{
                    todosBotones[i].classList.remove('animacionAbajoR');        
                };
                seleccion.classList.remove('animacionArribaR');
                sessionStorage.setItem('running','no');
                let bug = document.querySelector('.sobreMi');
                if (todosBotones[i].className !== bug.className && seleccion.className !== bug.className && bug.className === 'sobreMi animacionAbajoR'){
                    console.log(bug.className);
                    console.log('here');
                    bug.classList.remove('animacionAbajoR');
                }; 
            }, 900);
        };
    };

};