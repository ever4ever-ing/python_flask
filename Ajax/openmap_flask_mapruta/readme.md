## script.js

El código está estructurado en varias secciones, cada una con una funcionalidad específica. Aquí tienes una descripción de cada sección:

1. **Saludo**:
   - Captura el evento de clic en el botón con id `send-btn`.
   - Obtiene el valor del campo de texto con id `name`.
   - Envía una solicitud POST al servidor con el nombre capturado.
   - Muestra la respuesta del servidor en el elemento con id `response`.

2. **Buscar ubicación**:
   - Captura el evento de clic en el botón con id `location-btn`.
   - Obtiene el valor del campo de texto con id `place`.
   - Envía una solicitud POST al servidor con el lugar capturado.
   - Muestra la respuesta del servidor en el elemento con id `location-response`.

3. **Inicializar el mapa**:
   - Inicializa un mapa centrado en coordenadas [0, 0] con un zoom de nivel 2.
   - Añade una capa de mosaico de OpenStreetMap al mapa.

4. **Buscar ubicación y mostrar en el mapa**:
   - Captura el evento de clic en el botón con id `location-btn` (repetido).
   - Obtiene el valor del campo de texto con id `place`.
   - Envía una solicitud POST al servidor con el lugar capturado.
   - Muestra la respuesta del servidor en el elemento con id `location-response`.
   - Mueve el mapa a la ubicación obtenida y añade un marcador en esa ubicación.

5. **Variables para almacenar lugares seleccionados**:
   - Declara las variables `places` para almacenar los lugares seleccionados y `routeLayer` para la capa de la ruta.

6. **Añadir un lugar a la lista**:
   - Captura el evento de clic en el botón con id `add-place-btn`.
   - Obtiene el valor del campo de texto con id `route-place`.
   - Envía una solicitud POST al servidor con el lugar capturado.
   - Añade el lugar a la lista `places` y muestra el lugar en una lista en el DOM.
   - Añade un marcador en el mapa para el lugar seleccionado.

7. **Generar ruta**:
   - Captura el evento de clic en el botón con id `generate-route-btn`.
   - Verifica que haya al menos dos lugares en la lista `places`.
   - Construye una URL para la API de OSRM con las coordenadas de los lugares seleccionados.
   - Envía una solicitud GET a la API de OSRM para obtener la ruta.
   - Muestra la ruta en el mapa y ajusta el mapa para que se ajuste a la ruta.

Cada sección está claramente separada y tiene una funcionalidad específica, lo que facilita la comprensión y el mantenimiento del código.

