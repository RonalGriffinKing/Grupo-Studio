let letra = document.getElementById("letra").value.uppercase();
let botonenviar=document.getElementById("enviar");

let palabras=["HTML","CSS","JS"]
let random = Math.floor(Math.random()*palabras.length);
let palabraSecreta=palabras[random];

let letrasAdivinadas = new Array(palabraSecreta.length).fill("_");

let MostrarPalabra = document.getElementById("palabratag")

MostrarPalabra.innerHTML="_ ".repeat(palabraSecreta.length);

botonenviar.addEventListener("click",function(){
    if(palabraSecreta.includes(letra)){
        for(let i=0;i<palabraSecreta.length;i++){
            if(palabraSecreta[i]==letra){
                letrasAdivinadas[i]=letra;
            }    
        }
        document.getElementById("palabratag").innerHTML=letrasAdivinadas.join(" ");
    }


})
