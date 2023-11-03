const formularioIntegrante = document.getElementById("formIntegranteCSTF");
const inputs = document.querySelectorAll("#formIntegranteCSTF input");



const campos = {
	campo1: false, //nombre
	campo2: false, //apellido
	campo3: false, //dni
	campo4: false, //matricula
    fecha: false, //correo
}

function validarFecha(){
    let fechaValor = document.getElementById("fecha_alta_cs").value;
    let fechaActual= new Date();
    let fechaForm = new Date(fechaValor);
    console.log(fechaActual);
   console.log(fechaForm);
   console.log(fechaForm < fechaActual);

    if(fechaForm < fechaActual){
       document.querySelector(`#grupo__3 .formulario__input-error`).classList.remove("formulario__input-error-activo");
       campos.fecha= true;
    }else{
       document.querySelector(`#grupo__3 .formulario__input-error`).classList.add("formulario__input-error-activo");
       campos.fecha=false;
    }
 }
 

formularioIntegrante.addEventListener('submit', (e)=>{
    e.preventDefault();
    validarFecha();
    if(campos.fecha){
        document.getElementById('formulario__mensaje-exito').classList.add('formulario__mensaje-exito-activo');
        document.getElementById('formulario__mensaje').classList.remove('formulario__mensaje-activo');
        setTimeout(() => {
			document.getElementById('formulario__mensaje-exito').classList.remove('formulario__mensaje-exito-activo');
		}, 5000);
        formularioIntegrante.submit();
    }else{
        document.getElementById('formulario__mensaje').classList.add('formulario__mensaje-activo');
        setTimeout(() => {
			document.getElementById('formulario__mensaje').classList.remove('formulario__mensaje-activo');
		}, 5000);
    }
});