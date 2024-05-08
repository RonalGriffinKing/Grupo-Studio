let Alerta = document.getElementById("Alerta");
let Error = document.getElementById("Error");
let Aprobado = document.getElementById("Aprobado");
let Peligro = document.getElementById("Peligro");

Alerta.addEventListener("click", alerta);
function alerta(){
    console.log("Alerta");
    Swal.fire({
        icon: "The internet",
        title: "Oops...",
        text: "Alerta",
        confirmButtonText: "Entendido",
        footer: '<a href="#">Why do I have this issue?</a>',
        background:" url(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRxfOgKnpylITn1mFZQZMjWz-XsaOfTUxR0lP7uoyihFw&s)",
        background:"width: 100%; height: 100%;"
    });

}

Error.addEventListener("click", error);
function error(){
    console.log("Error");
    Swal.fire({
        icon: "error",
        title: "Oops...",
        text: "Error no tenemos ideas",
        footer: '<a href="#">Why do I have this issue?</a>'
      });
}

Aprobado.addEventListener("click", aprobado);
function aprobado(){
    console.log("Aprobado");
    Swal.fire({
        icon: "success",
        title: "Aprobado",
        text: "Aprobado",
        footer: '<a href="#">Why do I have this issue?</a>'
      });
}

Peligro.addEventListener("click", peligro);
function peligro(){
    console.log("Peligro");
    Swal.fire({
        icon: "warning",
        title: "Peligro",
        text: "Peligro un poco de fifes por aqui",
        footer: '<a href="#">Why do I have this issue?</a>'
      });
}
