let menos = document.getElementById("izquierda");
let mas = document.getElementById("derecha");
let cantidad = document.getElementById("cantidad");
let valor_cantidad = Number(cantidad.textContent);
let precio=document.getElementById("precio");
menos.addEventListener("click", () => {
    valor_cantidad--;
    cantidad.innerHTML = valor_cantidad;
});

mas.addEventListener("click", () => {
    valor_cantidad++;
    cantidad.innerHTML = valor_cantidad;
    
});





let img_principal=document.getElementById("img");
let colores=document.getElementById("colores");
colores.addEventListener("change",()=>{
    if(colores.value=="azul"){
        img_principal.src="https://th.bing.com/th/id/OIP.hTlsg5ZlqE8sagAvNuFNuAHaFR?rs=1&pid=ImgDetMain"
        precio.innerHTML=25
        precio
    }
    if(colores.value=="rojo"){
        img_principal.src="https://www.pinpng.com/pngs/m/228-2280940_this-little-guy-is-from-stardew-valley-hd.png"
        precio.innerHTML=25
    }
    if(colores.value=="rainbow"){
        img_principal.src="https://ih1.redbubble.net/image.878990140.0692/bg,f8f8f8-flat,750x,075,f-pad,750x1000,f8f8f8.jpg"
        precio.innerHTML=30
    }
    if(colores.value==""){
        img_principal.src="https://i.etsystatic.com/36789232/r/il/351768/4122726944/il_1080xN.4122726944_627q.jpg"
        precio.innerHTML=25
    }
})

function calcular_total(){
    let total=precio.innerHTML*valor_cantidad
    document.getElementById("total").innerHTML=total
}

