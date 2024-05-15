

let favorito1 = document.getElementById("like1");
let favorito2 = document.getElementById("like2");

let imagenportada1 = document.getElementById("imagen-portada1");
let imagenportada2 = document.getElementById("imagen-portada2");

let textoFavorito = document.getElementById("texto-Favorito");
let favorito3 = document.getElementById("imagen-Favorito");



let misFavoritos={
    "miArtitista": "Lana del Rey",
    "misAlbum": [],
};

favorito1.addEventListener("click", () => {
    if (misFavoritos.misAlbum=="Lust for life"){
        misFavoritos.misAlbum.pop();
        console.log(misFavoritos);
        mostrarFavoritos()
    }
    else{
        misFavoritos.misAlbum.push("Lust For Life");
        console.log(misFavoritos);
        mostrarFavoritos()
    }
    

});
favorito2.addEventListener("click", () => {
    if (misFavoritos.misAlbum=="Norman Fucking Rockwell"){
        misFavoritos.misAlbum.pop();
        console.log(misFavoritos);
        mostrarFavoritos()
    }
    else{
        misFavoritos.misAlbum.push("Norman Fucking Rockwell");
        console.log(misFavoritos);
        mostrarFavoritos()
    }
});



function mostrarFavoritos(){

    let favoritos = misFavoritos.misAlbum;
    let div = document.getElementById("ALBUMF");


    



    favoritos.forEach(element => {
        let div2 = document.createElement("div");
        div2.innerHTML = element;
        div.appendChild(div2);
    });
}
