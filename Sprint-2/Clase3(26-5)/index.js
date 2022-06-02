function obtenerSuma(){

    let cantidadCaja = document.getElementById("caja").value
    
    let cantidadCtaCte = document.getElementById("corriente").value
    
    let cantidadSueldo = document.getElementById("sueldo").value

    let cantidadTotal = cantidadCaja+cantidadCtaCte+cantidadSueldo;

    document.getElementById("saldo").value = cantidadTotal;

}