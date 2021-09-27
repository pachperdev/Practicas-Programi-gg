var d = document.getElementById("dibujoCanvas");
var lienzo = d.getContext("2d");

function dibujarLinea(color, xinicial, xfinal, yinicial, yfinal){
  lienzo.beginPath(); // buscamos en lapiz y lo ponemos sobre la mesa.
  lienzo.strokeStyle = color; // seleccionamos el color. esto es un atributo o variable.
  lienzo.moveTo(xinicial, yinicial); // seleccionamos la posicion inicial.
  lienzo.lineTo(xfinal, yfinal); // vamos a hacer una linea recta.
  lienzo.stroke(); // luego debujamos la linea. trazamos la linea.
  lienzo.closePath(); // levantamos el lapiz y cerramos el camino.
}
var colorlineas = "black";
dibujarLinea(colorlineas, 1,1,1,299);
dibujarLinea(colorlineas, 1,299,299,299);

var limite = 30;

for(l = 0; l < limite; l++) // inferior izquierda
{
  yi = 10 * l;
  xf = 10 * (l + 1);
  dibujarLinea(colorlineas,0,yi,xf,300);
}

for(l = 0; l < limite; l++) //superior dereha
{
  yi=300-10*l;
  xf=290-10*l
  dibujarLinea(colorlineas,300,yi,xf,0);
}
