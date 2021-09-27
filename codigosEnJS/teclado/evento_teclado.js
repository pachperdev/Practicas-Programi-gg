var teclas = { // este es un objeto, es una variable que contiene varias variables.
  UP: 38,
  DOWN: 40, // por lo general las variables perpertuas se escriben en MAYUSCULAS.
  LEFT: 37,
  RIGHT:39 // la ultima subvariable no se le pone la coma(,).
};
document.addEventListener("keyup",dibujarTeclado);
var cuadrito = document.getElementById("area_dibujo");
var lienzo = cuadrito.getContext("2d");

function dibujarLinea(color, xinicial, yinicial, xfinal, yfinal, lienzo)
{
  lienzo.beginPath();
  lienzo.strokeStyle = color;
  lienzo.moveTo(xinicial, yinicial);
  lienzo.lineTo(xfinal, yfinal);
  lienzo.stroke();
  lienzo.closePath();
}

var colorlinea = "red";
var x = 150;
var y = 150;
var movimieto = 10;
function dibujarTeclado(evento)
{
  if (evento.keyCode == teclas.UP)
  {
  console.log("arriba crack")
  dibujarLinea(colorlinea, x, y, x, y - movimieto, lienzo);
  y = y - movimieto;
  }
  if (evento.keyCode == teclas.DOWN)
  {
  console.log("abajo crack")
  dibujarLinea(colorlinea, x, y, x, y + movimieto, lienzo);
  y = y + movimieto;
  }
  if (evento.keyCode == teclas.RIGHT)
  {
  console.log("derecha crack")
  dibujarLinea(colorlinea, x, y, (x + movimieto), y, lienzo);
  x = x + movimieto;
  }
  if (evento.keyCode == teclas.LEFT)
  {
  console.log("izquierda crack")
  dibujarLinea(colorlinea, x, y, x - movimieto, y, lienzo);
  x = x - movimieto;
  }
}
