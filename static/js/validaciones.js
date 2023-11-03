const formularioAlumno = document.getElementById("formAlumno");
const inputs = document.querySelectorAll("#formAlumno input");

const expresiones = {
	nombre: /^[a-zA-ZÀ-ÿ\s]{2,40}$/, // Letras y espacios, pueden llevar acentos.
	apellido: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
    correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
    matricula: /^\d{5}$/,
    dni: /^\d{8}$/
}

const campos = {
	campo1: false, //nombre
	campo2: false, //apellido
	campo3: false, //dni
	campo4: false, //matricula
    campo5: false, //correo
}

function validarFormulario(e){
    switch(e.target.name){
        case 'nombre':
            validarCampo(expresiones.nombre, e.target, '1');
        break;
        case 'apellido':
            validarCampo(expresiones.apellido, e.target, '2');
        break;
        case 'dni':
            validarCampo(expresiones.dni, e.target, '3');
        break;
        case 'matricula':
            validarCampo(expresiones.matricula, e.target, '4');
        break;
        case 'correo':
            validarCampo(expresiones.correo, e.target, '5');
        break;
    }
}

function validarCampo(expresion, input, campo){
    if(expresion.test(input.value)){
        document.getElementById(`grupo__1`).classList.remove('formulario__grupo-incorrecto');
        document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.remove('formulario__input-error-activo');
        campos[`campo${campo}`] = true;
    }else{
        document.getElementById(`grupo__${campo}').classList.add('formulario__grupo-incorrecto`);
        document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.add('formulario__input-error-activo');
        campos[`campo${campo}`] = false;
    }
}

inputs.forEach((input)=>{
    input.addEventListener('keyup', validarFormulario)
    input.addEventListener('blur', validarFormulario)
})

formularioAlumno.addEventListener('submit', (e)=>{
    e.preventDefault();
    if(campos.campo1 && campos.campo2 && campos.campo3 && campos.campo4 && campos.campo5){
        
        document.getElementById('formulario__mensaje-exito').classList.add('formulario__mensaje-exito-activo');
        document.getElementById('formulario__mensaje').classList.remove('formulario__mensaje-activo');
		
        setTimeout(() => {
			document.getElementById('formulario__mensaje-exito').classList.remove('formulario__mensaje-exito-activo');
		}, 5000);

        formularioAlumno.submit();
    }else{
        document.getElementById('formulario__mensaje').classList.add('formulario__mensaje-activo');
        setTimeout(() => {
			document.getElementById('formulario__mensaje').classList.remove('formulario__mensaje-activo');
		}, 5000);
    }

})



