const form = document.querySelector('#rifa-form');

form.addEventListener('submit', async (e) => {
	e.preventDefault();

	const nombre = document.querySelector('#nombre').value;
	const celular = document.querySelector('#celular').value;
	const email = document.querySelector('#email').value;
	const numRifa = document.querySelector('#numRifa').value;

	const data = {
		nombre: nombre,
		cel: celular,
		email: email,
		numeros: [numRifa.split(',').map(Number)]
	};

	try {
		const response = await fetch('http://127.0.0.1:8000/rifapost', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(data)
		});

		const responseData = await response.json();
		console.log(responseData);
		
		// Agregamos una ventana popup para mostrar que se envió correctamente el formulario
		alert('Formulario enviado correctamente');

		// Borramos los valores del formulario
		document.querySelector('#nombre').value = '';
		document.querySelector('#celular').value = '';
		document.querySelector('#email').value = '';
		document.querySelector('#numRifa').value = '';

	} catch (error) {
		console.error(error);
	}
});
