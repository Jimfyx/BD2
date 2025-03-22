# Buenas Practicas MongoDB


## Los campos
Solo pueden poner banderas

personas:{

    nombres:[
        {
        nombre:"Roberto",
        tipo:"primer",
        abreviado:"Bob"
        },
        {
        nombre:"Guillermo"
        }
    ],

    activo:0

}

## Inicio de Modelaje

* Que nos van a preguntar
* Cuales son las consultas

** Hotwheels
* Que color es el carro
* * Que modelo
* * Que pedo
* * Que edicion
* * Año de Fabricacion
* * Numero de Ruedas
* * Categoria
* * Precio

Modelo:
    * Incrustar, todo lo que podamos

Hw: {
    color: --array
    [
        {
            color:"anaranjado",
            tipo:"abundante",
        },
        {
            color:"azul",
            tipo:"logo",
        },
        {
            color:"blanco"
            empaque:true,
        }
    ],
    precios:
    [
        {
            precio:24,
            moneda:"Quetzales",
            fecha: 2024-08-09,
            activo:0
        },
        {
            precio:22,
            moneda:"Quetzales",
            fecha: 2025-08-09,
            activo:1
        }
    ]   