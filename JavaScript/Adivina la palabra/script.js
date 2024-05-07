let letra = document.getElementById("letra");

let botonenviar=document.getElementById("enviar");
let palabras=["HTML","CSS","JS"]
let random = Math.floor(Math.random()*palabras.length);
let palabraSecreta=palabras[random];
let letrasAdivinadas = new Array(palabraSecreta.length).fill("_");
let MostrarPalabra = document.getElementById("MostrarPalabra");
MostrarPalabra.innerHTML=letrasAdivinadas.join(" ");




botonenviar.addEventListener("click",function(){
    let letrita=letra.value.toUpperCase();
    console.log(letrita);
    if(palabraSecreta.includes(letrita)){
        console.log("if");
        for(let i=0;i<palabraSecreta.length;i++){
            console.log("for");
            if(palabraSecreta[i]==letrita){
                letrasAdivinadas[i]=letrita;
            } 
        }
        MostrarPalabra.innerHTML=letrasAdivinadas.join(" ");    

    }else{
        console.log("else");
        alert("la letra no existe");
    }
    console.log(letrasAdivinadas);
    if(letrasAdivinadas.join("")==palabraSecreta){
        alert("Ganaste");
    }
})
