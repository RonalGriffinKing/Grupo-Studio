let Dia=document.getElementById("Dia");
let Mes=document.getElementById("Mes");
let Anio=document.getElementById("Anio");
let Informacion=document.getElementById("Informacion");
let Calcular=document.getElementById("Calcular");



Calcular.addEventListener("click",()=>{
   if(Dia.value=="" || Mes.value=="" || Anio.value==""){
        Informacion.innerHTML="Todos los campos son obligatorios";
        Informacion.style.color="red";
        Informacion.style.fontSize="20px";
   }else{
        if(Dia.value<1 || Mes.value<1 || Anio.value<1){
            Informacion.innerHTML="Informacion Invalida";
            
        }else{
             AnioActual=parseInt(new Date().getFullYear());
            if(Dia.value>31 || Mes.value>12 || Anio.value>AnioActual){
                Informacion.innerHTML="Informacion Invalida";
            }else{
                Dia.value=parseInt(Dia.value);
                Mes.value=parseInt(Mes.value);
                Anio.value=parseInt(Anio.value);
                MesActual=parseInt(new Date().getMonth())+1;
                DiaActual=parseInt(new Date().getDate());
                Edad=AnioActual-Anio.value;
                Meses=MesActual-Mes.value;
                if(Meses<0){
                    Edad--; //Es necesario para que no de negativo entonces le restamos uno
                    Meses=12+Meses;
                }
                Dias=DiaActual-Dia.value;
                if(Dias<0){
                    Meses--;
                    Dias=30+Dias;
                }


            }
            Informacion.innerHTML="Tienes "+Edad+" años y "+Meses+" meses" +" y "+Dias+" dias";
        }
    }
  



})