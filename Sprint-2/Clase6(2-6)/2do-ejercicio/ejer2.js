let NombreArray = [];
let elemento = document.getElementById('elemento');

function addNombre(){
    let nombre = document.getElementById('nombreInput').value;
    NombreArray.push(nombre);
}

function borrarNombre(){
    let nombre = document.getElementById('nombreInput').value;
    for(let nomb of NombreArray){
        if(nomb == nombre){
            NombreArray.splice(NombreArray.indexOf(nomb));
        }
    }
}

function printNombre(){
    console.log(NombreArray);
    for(let nomb of NombreArray){
        let elemento2 = document.createElement('li');
        elemento.innerHTML= `Nombre: ${nomb}`;
        elemento2.classList.add('list-group-item');
        elemento.appendChild(elemento2);

    }
}
