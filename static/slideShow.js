// Define la nueva cadena que quieres usar
let srcList = [
    '..\\static\\mem0g4to.png',
    '..\\static\\mem0p3rro.png',
    '..\\static\\mem0bo4rd.png',
    '..\\static\\mem0r3sult.png',
    '..\\static\\mem0mainscreen.png'
]

// Actualiza los atributos src y srcset del elemento <img>
// Itera sobre la lista de cadenas
async function loopWithDelay(srcList, imgElement) {
    for (let i = 0; i < srcList.length; i++) {
      let currentSrc = srcList[i];
      // Actualiza los atributos src y srcset del elemento <img>
      imgElement.classList.add('aparecer'); // Agregamos la clase .aparecer al elemento
        setTimeout(() => { // Esperamos a que termine la animación antes de ocultar el elemento
            imgElement.classList.remove('aparecer'); // Removemos la clase .aparecer del elemento
        }, 500);
      imgElement.src = currentSrc;
      imgElement.srcset = currentSrc + ' 500w,' + currentSrc + ' 800w,' + currentSrc + ' 816w';
      // Wait for 1 second before continuing to the next iteration
      await new Promise(resolve => setTimeout(resolve, 4000));
    }
    // Llama a la función de nuevo para crear un bucle infinito
    loopWithDelay(srcList, imgElement);
  };

setTimeout(function slideSHow() {
    // Selecciona el elemento <img> utilizando su clase
    let imgElement = document.querySelector('.mem0mainscreen-27');
    loopWithDelay(srcList,imgElement);    
}, 4000);
