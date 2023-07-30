function animacionAbajo(todosBotones,idSeleccion,seleccion) {   
//El bucle nos permite encontrar el elemento que originalmente está mostrandose en plantilla.
    for (let i = 0; i<todosBotones.length; i++){
        if (todosBotones[i].style.display === 'inline' ){
//Si el algun elemento necesita un ajuste en animación debido a su posición en plantilla se asigna la variante A.
            if (idSeleccion !== 'sobreMi'){
                seleccion.classList.add('animacionAbajoA');
            }else{
                seleccion.classList.add('animacionAbajo');
            };
            seleccion.style.display = 'inline';           
            if (todosBotones[i] !== seleccion){
                todosBotones[i].classList.remove('hoverA');
                if(todosBotones[i].className !== 'contacto'){
                    todosBotones[i].classList.add('animacionArriba');                
                }else{
                    todosBotones[i].classList.add('animacionArribaA');
                };
                console.log('INICIO');
            };

//Se elige un timeout con un desfase antes para que el elemento no vuelva a aparecer en pantalla al terminar la animación.
            setTimeout(function() {
                if (todosBotones[i] !== seleccion){
                    todosBotones[i].style.display = 'none';    
                    //Se elige un timeout despúes, para que una nueva animación no interrumpa la animación.
                    setTimeout(function() {
                        sessionStorage.setItem('running','no');
                        seleccion.classList.add('hoverA');
                        console.log('FINAL');                                           
                    }, 50);
                }; 
                if(todosBotones[i].className !== 'contacto'){
                    todosBotones[i].classList.remove('animacionArriba');                
                }else{
                    todosBotones[i].classList.remove('animacionArribaA');
                };
                if (idSeleccion !== 'sobreMi'){
                    seleccion.classList.remove('animacionAbajoA');
                }else{
                    seleccion.classList.remove('animacionAbajo');
                };
                let bug1 = document.querySelector('.contacto');
                bug1.classList.remove('animacionArribaA');             
            }, 970);
        };
    };

};

function animacionArriba(todosBotones,idSeleccion,seleccion) {
    for (let i = 0; i<todosBotones.length; i++){
        if (todosBotones[i].style.display === 'inline' ){
            if (todosBotones[i] !== seleccion){
                console.log('INICIO');
                todosBotones[i].classList.remove('hoverA');
                if(todosBotones[i].className !== 'sobreMi'){
                    todosBotones[i].classList.add('animacionAbajoAR');                    
                }else{
                    todosBotones[i].classList.add('animacionAbajoR');                    
                };
            };
            if(idSeleccion !== 'contacto'){
                seleccion.classList.add('animacionArribaR');
            }else{
                seleccion.classList.add('animacionArribaAR');
            };          
            seleccion.style.display = 'inline';
            setTimeout(function() {
                if (todosBotones[i] !== seleccion){
                    todosBotones[i].style.display = 'none';    
                setTimeout(function() {
                    seleccion.classList.add('hoverA');
                    sessionStorage.setItem('running','no');
                    console.log('FINAL');                                           
                }, 50);
                }; 
                if(todosBotones[i].className !== 'sobreMi'){
                    todosBotones[i].classList.remove('animacionAbajoAR');                  
                }else{
                    todosBotones[i].classList.remove('animacionAbajoR');        
                };
                if(idSeleccion !== 'contacto'){
                    seleccion.classList.remove('animacionArribaR');
                }else{
                    seleccion.classList.remove('animacionArribaAR');
                };          
                let bug = document.querySelector('.sobreMi');
                if (todosBotones[i].className !== bug.className && seleccion.className !== bug.className && bug.className === 'sobreMi animacionAbajoR'){
                    bug.classList.remove('animacionAbajoR');                
                };               
            }, 970);
        };
    };
};