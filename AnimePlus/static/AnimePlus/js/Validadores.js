

$(document).ready(function(){
	$("#form1").submit(function(evento){
		if(!valido()){
			alert("Formulario no valido");
			evento.preventDefault();
		}
	});
    $("[name='nombre']").blur(validarNombre);
    $("[name='correo']").blur(validarCorreo);    
    $("[name='fono']").blur(validarTelefono);
    $("[name='fecha']").blur(validarFecha);

});

function valido(){

	var valido = true;
    valido = validarNombre() && valido;
    valido = validarCorreo() && valido;
    valido = validarTelefono() && valido;
    valido = validarFecha() && valido;

	return valido;
}

function validarNombre() {
	$("#mensaje_nombre").html("");
	var nombre = $("[name='nombre']").val();
	nombre = $.trim(nombre);
	if(nombre.length == 0){
		$("#mensaje_nombre").html(
				"No puedes dejar el nombre en blanco");
		return false;
	}
	return true;
}

function validarCorreo() {
	$("#mensaje_correo").html("");
	var correo = $("[name='correo']").val();
	correo = $.trim(correo);
	if(correo.length == 0){
		$("#mensaje_correo").html(
				"No puedes dejar el correo en blanco");
		return false;
	}
	return true;
}

function validarTelefono() {
	$("#mensaje_fono").html("");
	var fono = $("[name='fono']").val();
	fono = $.trim(fono);
	if(fono.length == 0){
		$("#mensaje_fono").html(
				"No puedes dejar el telefono en blanco");
		return false;
	}
	return true;
}

function validarFecha() {
	$("#mensaje_fecha").html("");
	var fecha = $("[name='fecha']").val();
	var fecha = new Date(fecha);
	var hoy = new Date();
	if(fecha > hoy){
		$("#mensaje_fecha").html(					
			"Fecha no válida");
		return false;
	}
	if(fecha.getFullYear() < 1900){		
		$("#mensaje_fecha").html(
			"Fecha no válida");
		return false;
	}

	return true;
}