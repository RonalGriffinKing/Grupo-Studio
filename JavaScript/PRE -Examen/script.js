let favorito1 = document.getElementById("like1");
let favorito2 = document.getElementById("like2");

let imagenportada1 = document.getElementById("imagen-portada1");
let imagenportada2 = document.getElementById("imagen-portada2");

let textoFavorito = document.getElementById("texto-Favorito");
let favoritosList = document.getElementById("favoritos-list");

let corazon1 = document.getElementById("corazon1");
let corazon2 = document.getElementById("corazon2");

let misFavoritos = {
    "miArtista": "Lana del Rey",
    "misAlbum": [],
    "misImagenes": []
    
};

favorito1.addEventListener("click", () => {
    let album = "Lust For Life";
    let img = "https://www.lahiguera.net/musicalia/artistas/lana_del_rey/disco/8313/lana_del_rey_lust_for_life-portada.jpg";
    let index = misFavoritos.misAlbum.indexOf(album);
    if (index !== -1) {
        misFavoritos.misAlbum.splice(index, 1);
        misFavoritos.misImagenes.splice(index, 1);
        corazon1.style.color = "white";
    } else {
        misFavoritos.misAlbum.push(album);
        corazon1.style.color = "red";
        misFavoritos.misImagenes.push(img);

    }
    updateFavoritosList();
    console.log(misFavoritos);
});

favorito2.addEventListener("click", () => {
    let album = "Norman Fucking Rockwell";
    let img = "https://www.efeeme.com/wp-content/uploads/2019/08/lana-del-rey-norman-fucking-rockwell-01-08-19.jpeg";
    let index = misFavoritos.misAlbum.indexOf(album);
    if (index !== -1) {
        misFavoritos.misAlbum.splice(index, 1);
        misFavoritos.misImagenes.splice(index, 1);
        corazon2.style.color = "white";

    } else {
        misFavoritos.misAlbum.push(album);
        corazon2.style.color = "red";
        misFavoritos.misImagenes.push(img);
    }
    updateFavoritosList();
    console.log(misFavoritos);
});

function updateFavoritosList() {
    // Limpiar la lista de favoritos
    favoritosList.innerHTML = "";

    // Agregar cada álbum a la lista
    misFavoritos.misAlbum.forEach(album => {
       // Crear el contenedor principal
                // Asegúrate de que favoritosList use flexbox
        favoritosList.style.display = "flex";
        favoritosList.style.flexWrap = "wrap"; // Permitir que los elementos se envuelvan si es necesario
        favoritosList.style.gap = "10px"; // Espacio entre elementos (opcional)

        // Crear el contenedor principal para cada imagen y texto
        let div = document.createElement("div");
        div.style.textAlign = "center";
        
        div.style.width = "150px";
        div.style.height = "250px";

        // Crear y configurar la imagen
        let img = document.createElement("img");
        img.src = misFavoritos.misImagenes[misFavoritos.misAlbum.indexOf(album)];
        img.style.width = "100px";
        img.style.height = "100px";
        img.style.objectFit = "cover";

        // Crear y configurar el párrafo
        let p = document.createElement("p");
        p.textContent = album;
        p.style.textAlign = "center"; // Centrar el texto debajo de la imagen

        // Añadir la imagen y el párrafo al contenedor principal
        div.appendChild(img);
        div.appendChild(p);

        // Añadir el contenedor principal a la lista de favoritos
        favoritosList.appendChild(div);


    });

    // Mostrar FAVORITOS ACTIVOS
    


}
