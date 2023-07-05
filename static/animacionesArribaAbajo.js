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
            if(todosBotones[i].className !== 'contacto'){
                todosBotones[i].classList.add('animacionArriba');                
            }else{
                todosBotones[i].classList.add('animacionArribaA');
            };

            setTimeout(function() {
                if (todosBotones[i] !== seleccion){
                    todosBotones[i].style.display = 'none';    
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
                sessionStorage.setItem('running','no');
                let bug1 = document.querySelector('.contacto');
                bug1.classList.remove('animacionArribaA');                
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
            if(idSeleccion !== 'contacto'){
                seleccion.classList.add('animacionArribaR');
            }else{
                seleccion.classList.add('animacionArribaAR');
            };          
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
                if(idSeleccion !== 'contacto'){
                    seleccion.classList.remove('animacionArribaR');
                }else{
                    seleccion.classList.remove('animacionArribaAR');
                };          
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