/* let nombre = prompt("Ingresa tu nombre");

let temperatura = prompt("¿Cual es la temperatura?");

let recomendacion

if (temperatura>=0 && temperatura<=16){ 
    temperatura=("está fresco para pasear,");
    recomendacion=("lleva un abrigo ligero");
} else if (temperatura>16 && temperatura<=33){ 
    temperatura=("va a ser un día hermoso");
    recomendacion=null;
} else { 
    temperatura=("hace mucho frío,");
    recomendacion=("anda bien abrigado");
}

document.write("Hola " + nombre);
document.write("<br/> Hoy " + temperatura + " " + recomendacion); */

let temperatura = document.getElementById("btn").value;
let elemento = document.getElementById("texto");

