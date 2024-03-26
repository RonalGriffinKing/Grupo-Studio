// Arrays
let nombres=["Ronal","Felipe","Marcela"]

console.log("Esta es tu lista de nombres: ",nombres)

// push agrega un elemento al final
console.log("Agregarmos un nuevo nombre Carlos")
nombres.push("Carlos")
console.log(nombres)

// pop elimina el ultimo elemento
nombres.pop()
console.log("Eliminamos el ultimo nombre Carlos")
console.log(nombres)

// shift elimina el primer elemento
nombres.shift()
console.log("Eliminamos el primer nombre Ronal")
console.log(nombres)

// unshift agrega un elemento al principio
nombres.unshift("Steven")
console.log("Agregamos un nuevo nombre Steven al principio")
console.log(nombres)

// splice elimina elementos
nombres.splice(1,1)
console.log("Eliminamos el segundo nombre Felipe")
console.log(nombres)

//Agregar elementos al array
nombres.push("Carlos","Carla","Ramon","Marcelo")
console.log("Agregamos 4 nombres")
console.log(nombres)


//Ordenar los elementos del array
nombres.sort()
console.log("Ordenamos los nombres")
console.log(nombres)

//Invertir los elementos del array
nombres.reverse()
console.log("Invertimos los nombres")
console.log(nombres)

//Iterar sobre los elementos del array
nombres.forEach((elemento)=>console.log(elemento))

//Elementos 
let persona={
    nombre:"Carlos",
    edad:30,
    genero:"Masculino",
    amigos:["Steven","Marcelo","Carla","Carlos"],
    libros:{
        libro1:"Harry Potter",
        libro2:"Cancion de hielo y fuego",
    }

}
console.log(persona)
console.log(persona.libros.libro2)
console.log(persona.amigos[1])


let alumnos=[
    {
        nombre:"Carmino",
        edad:56,
        genero:"Masculino",
        casado:false,
        amigos:["Steven","Marcelo","Carla","Carlos"],
        libros:{
            libro1:"Harry Potter",
            libro2:"Cancion de hielo y fuego",
    }
    },
    {
        nombre:"Felipe",
        edad:12,
        genero:"Masculino",
        casado:true,
        amigos:["Steven","Marcelo","Carla","Carlos"],
        libros:{
            libro1:"Harry Potter",
            libro2:"Cancion de hielo y fuego",
        }
    
    }
    ,
    {
        nombre:"Marcela",
        edad:20,
        genero:"Femenino",
        casado:true,
        amigos:["Steven","Marcelo","Carla","Carlos"],
        libros:{
            libro1:"Harry Potter",
            libro2:"Cancion de hielo y fuego",
        }
    }
]

console.log(alumnos)

//Iterar sobre el array de objetos

console.log(alumnos[0].libros.libro1) //alumnos[0].libros.libro1


//Ejercicio 1 : dado el array de objetos recien creado, crea una funcion que devuelva un nuevo array con todos los alumnos casados
console.log("Ejercicio 1")
function casados(alumnos){
    let casados=[]
    for(let i=0;i<alumnos.length;i++){
        if(alumnos[i].casado==true){
            casados.push(alumnos[i].nombre)
        }
    }
    return casados
}
console.log("Alumnos casados: ",casados(alumnos))

//Ejercicio 2: 