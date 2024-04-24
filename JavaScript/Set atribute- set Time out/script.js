
//Obtengo los elementos HTML
let contador = document.getElementById('contador');

let clicks = document.getElementById('clicks');

let caja = document.getElementById('caja');

//Variables Para contar los clicks
let cont = 0;

//variable para verificar si el tiempo terminado
let tiempoTerminado = false;

// Colores disponibles para cambiar el color de fondo

let colores = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink'];


//Numero aleatorio para seleccionar un color de fondo
let aleatorio=Math.floor(Math.random() * colores.length);

//Funcion para cambiar el color de fondo
caja.addEventListener('click', function(){

    if(!tiempoTerminado){
        cont++;
        clicks.innerHTML = cont;
        caja.style.backgroundColor = colores[aleatorio];
        aleatorio = Math.floor(Math.random() * colores.length);
    }
})






//Funcion para contador

function iniciarContador(segundos) {
    contador.innerHTML = segundos;

    if (segundos == 0) { // Si el tiempo es igual a 0
        contador.innerHTML = 'Tiempo Terminado!';
        tiempoTerminado = true;
        return;

    } else {
        tiempoTerminado = false;
    }
    
    //llamamos recursivamente la función para decrementar el tiempo
    setTimeout(function () {
        iniciarContador(segundos - 1);
    }, 1000);
}

iniciarContador(10)