# README

## Sin recarga de página
AJAX permite el uso de formatos como JSON para enviar y recibir datos, facilitando la integración con otros servicios y APIs.
En este ejemplo, se envía un formulario a un servidor Flask mediante una solicitud POST y se actualiza la página con la respuesta sin recargarla.


1. El usuario escribe su nombre y hace clic en "Enviar".
2. AJAX envía el nombre al servidor Flask mediante una solicitud POST.
3. Flask procesa la solicitud y devuelve un mensaje JSON.
3. El navegador actualiza la página dinámicamente con la respuesta

Con AJAX, los datos se envían al servidor de manera asíncrona, lo que permite actualizar partes específicas de la página sin recargarla.
Con request.form, normalmente el formulario se envía como una solicitud POST estándar, lo que recarga toda la página después del envío.
