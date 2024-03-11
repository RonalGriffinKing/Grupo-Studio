/**
 * 
 * Dado una lista l =[10, 20, 30, 40, 50, 60, 30, 80, 90, 100] busca dentro del array el número 50 y devuelve su posición.
 * imprimelo por pantalla y ek numero de veces que aparece en la lista.
 * 
 * si el array no contiene el numero, escribir un mensaje indicando que no existe
 */

function prueba() {
    
    let lista=[];
    let numero=document.getElementById("input").value;
    console.log("la lista es: "+ lista)
    let memoria=[];
    let contador=0;
    let posición;
    for (let i= 0; i< lista.length; i++){
        if (lista[i] == numero){
            posición = i;
            memoria.push(i);
            numero = lista[i];
            contador++;
        }
    }
    if(numero == undefined){
        console.log("no existe")
    }
    console.log("la cantidad de veces que aparece el "+ numero +" es: "+ contador)
    console.log("el numero es: "+ numero)
    console.log("la posición es: "+ posición)
    console.log(memoria)
}