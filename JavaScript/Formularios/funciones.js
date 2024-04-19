
let selecion = document.getElementById("selecion");

selecion.addEventListener("change",()=>{
    if(selecion.value=="uno"){
        document.getElementById("contenedor-buscotrabajo").style.display="block"
        
        document.getElementById("contenedor-buscopersonal").style.display="none"
        document.getElementById("contenedor-suscribirme").style.display="none"
    }
    if(selecion.value=="dos"){
        document.getElementById("contenedor-buscotrabajo").style.display="none"
        document.getElementById("contenedor-buscopersonal").style.display="block"
        document.getElementById("contenedor-suscribirme").style.display="none"
    }
    if(selecion.value=="tres"){
        document.getElementById("contenedor-buscotrabajo").style.display="none"
        document.getElementById("contenedor-buscopersonal").style.display="none"
        document.getElementById("contenedor-suscribirme").style.display="block"
    }
    if(selecion.value=="0"){
        document.getElementById("contenedor-buscotrabajo").style.display="none"
        document.getElementById("contenedor-buscopersonal").style.display="none"
        document.getElementById("contenedor-suscribirme").style.display="none"
    }

})