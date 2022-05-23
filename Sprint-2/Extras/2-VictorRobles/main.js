// alert("Hola mundo");
var nombre = "Daniela";
var altura = 160;

var concatenacion = nombre + " " + altura;

var datos = document.getElementById("datos");
datos.innerHTML = `
    <h1>Soy la caja de datos</h1>
    <h2>Mi nombre es: ${nombre}</h2> 
    <h3>Mido: ${altura} cm</h3>
`;
