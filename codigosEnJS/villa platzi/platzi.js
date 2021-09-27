


var vp = document.getElementById("villaplatzi"); //nos traemos a villaplatzi
var papel = vp.getContext("2d"); // nos traemos el papel, lienzo y el coxtexto

var fondo = { // hacemos un objeto para el fondo del jueguito
  url: "tile.png",
  cargaOK: false
}
var vaca = { // hacemos un objeto para la vaca
  url: "vaca.png",
  cargaOK: false
};

var cantidad = aleatorio(1, 10); // asignamos un numero aleatorio entre 1 y 10, con una
//funcion llamada aleatorio.

fondo.imagen = new Image(); // le dicimos a js que fondo.imagen es una imagen.
fondo.imagen.src = fondo.url; // le decimo a js la rura de la imagen.
fondo.imagen.addEventListener("load", cargarFondo); // sensor para saber si fondo cargo

vaca.imagen = new Image();
vaca.imagen.src = vaca.url;
vaca.imagen.addEventListener("load", cargarVacas);

function cargarFondo()
{
  fondo.cargaOK = true;
  dibujar();
}
function cargarVacas()
{
  vaca.cargaOK = true;
  dibujar();
}

function dibujar()
{
  if(fondo.cargaOK)
  {
    papel.drawImage(fondo.imagen, 0, 0);
  }
  if(vaca.cargaOK)
  {
    console.log(cantidad);
    for(var v=0; v < cantidad; v++)
    {
      var x = aleatorio(0, 7);
      var y = aleatorio(0, 10);
      var x = x * 60;
      var y = y * 40;
      papel.drawImage(vaca.imagen, x, y);
    }
  }
}
function aleatorio(min, maxi)
{
  var resultado;
  resultado = Math.floor(Math.random() * (maxi - min + 1)) + min;
  return resultado;
}

/*
//codigo para generar un numero aleatorio entre un rango de valores.
var z;

for (var i = 0; i < 10; i++) {
  z = aleatorio(10, 20);
  document.write(z + ",");
}

function aleatorio(min, maxi)
{
var  resultado;
resultado = Math.floor(Math.random() * (maxi - min + 1)) + min;
return resultado;
}
*/
