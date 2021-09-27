var cuadrito = document.getElementById("area_dibujito");
var papel = cuadrito.getContext("2d");
var x;
var y;
var estado;
var boton = document.getElementById("botoncito");


boton.addEventListener("click", espacioCanvas) ;
cuadrito.addEventListener("mousedown",presionarMouse);  //cuando presionas click
cuadrito.addEventListener("mousemove",dibujarMouse);    //cuando mueves el mouse
cuadrito.addEventListener("mouseup",soltarMouse);       //cuando sueltas click


function espacioCanvas (evento)
{
    var anchoCanvas = document.getElementById("ancho_canvas");
    var altoCanvas = document.getElementById("alto_canvas");

    cuadrito.height = parseInt(altoCanvas.value);
    cuadrito.width = parseInt(anchoCanvas.value);

    var alto = cuadrito.height;
    var ancho = cuadrito.width;

    dibujarLinea("grey",1,1,1,alto, papel);
    dibujarLinea("grey",1,alto,ancho,alto, papel);
    dibujarLinea("grey",ancho,1,1,1, papel);
    dibujarLinea("grey",ancho,1,ancho,alto, papel);
}


function presionarMouse(evento)
{
  estado = 1;         //click presionado
  x = evento.layerX;
  y = evento.layerY;
}


function dibujarMouse (evento)
{

    var color = "blue";

    if (estado == 1)
    {   // solo se dibujara si esta el click del mouse presionado
    dibujarLinea(color, x, y, evento.layerX, evento.layerY, papel);
    }
    x = evento.layerX;
    y = evento.layerY;
}


function soltarMouse(evento)
{
    estado = 0;         // click suelto
    x = evento.layerX;
    y = evento.layerY;
}


function dibujarLinea(color, xinicial, yinicial, xfinal, yfinal, lienzo)
{
    lienzo.beginPath();
    lienzo.strokeStyle = color;
    lienzo.lineWidth = 3;
    lienzo.moveTo(xinicial,yinicial);
    lienzo.lineTo(xfinal,yfinal);
    lienzo.stroke();
    lienzo.closePath();
}
