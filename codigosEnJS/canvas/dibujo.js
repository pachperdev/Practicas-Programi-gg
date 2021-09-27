var texto = document.getElementById("texto_lineas"); // nos traemos la caja de texto
var boton = document.getElementById("botoncito"); // nos traemos el boton
var d = document.getElementById("dibujito"); //de esta manera obtenemos el "id"
//del cambas
boton.addEventListener("click", dibujoPorClick ); // ponemos un sensor a ver si ocurre algo

var ancho = d.width;
var lienzo = d.getContext("2d"); // obtenemos el espacio 2d o 3d de dibujo.

function dibujarLinea(color, xinicial, yinicial, xfinal, yfinal) // asi es una funcion.
{
  lienzo.beginPath(); // buscamos en lapiz y lo ponemos sobre la mesa.
  lienzo.strokeStyle = color; // seleccionamos el color. esto es un atributo o variable.
  lienzo.moveTo(xinicial, yinicial); // seleccionamos la posicion inicial.
  lienzo.lineTo(xfinal, yfinal); // vamos a hacer una linea recta.
  lienzo.stroke(); // luego debujamos la linea. trazamos la linea.
  lienzo.closePath(); // levantamos el lapiz y cerramos el camino.
}

function dibujoPorClick() // funcion que se activa cuando se da click sobre el boton.
{
  var lineas = parseInt(texto.value); // extraemos el valor de la caja de texto
  // con la linea "texto.value".
  var l = 0;
  var yi, xf;
  var colorcito = "#FAA";
  var espacio = ancho / lineas;

  for(l = 0; l < lineas; l++)
  {
    yi = espacio * l;
    xf = espacio * (l + 1);
    dibujarLinea(colorcito, 0, yi, xf, 300);
    console.log("Linea " + l);
  }

  dibujarLinea(colorcito, 1,1,1,299);
  dibujarLinea(colorcito, 1,299,299,299);
}
