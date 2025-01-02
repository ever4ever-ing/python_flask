// Saludo
/*
Captura el evento de clic en el botón con id="send-btn".
Obtiene el valor del campo de texto con id="name".
Usa fetch para enviar el nombre al endpoint /process como un JSON.
Recibe la respuesta del servidor y la muestra en el elemento con id="response".
Si ocurre un error, lo registra en la consola.
*/
document.getElementById('send-btn').addEventListener('click', () => {
    const name = document.getElementById('name').value;

    fetch('/process', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('response').innerText = data.message;
    })
    .catch(error => console.error('Error:', error));
});

// Buscar ubicación
/*
Captura el clic en el botón con id="location-btn".
Toma el valor del campo id="place".
Envía el valor al servidor con un POST al endpoint /location.
Si el servidor responde con éxito, actualiza el elemento con id="location-response" con los detalles del lugar.
Maneja errores mostrando un mensaje en la consola.
*/
document.getElementById('location-btn').addEventListener('click', () => {
    const place = document.getElementById('place').value;

    fetch('/location', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ place })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById('location-response').innerText = data.error;
        } else {
            document.getElementById('location-response').innerText =
                `Lugar: ${data.name}, Latitud: ${data.lat}, Longitud: ${data.lon}`;
        }
    })
    .catch(error => console.error('Error:', error));
});

// Inicializar el mapa (ubicación inicial predeterminada)
/*
Inicializa el mapa centrado en el mundo ([0, 0]) con zoom bajo (2).
Usa OpenStreetMap como capa base del mapa mediante L.tileLayer.
*/
let map = L.map('map').setView([0, 0], 2); // Coordenadas iniciales y zoom (mundo)

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Buscar ubicación y mostrar en el mapa
/*
Cuando se busca una ubicación, si es válida:
Centra el mapa en las coordenadas obtenidas (setView).
Añade un marcador en las coordenadas (L.marker).
Muestra un popup con el nombre del lugar.
*/
document.getElementById('location-btn').addEventListener('click', () => {
    const place = document.getElementById('place').value;

    fetch('/location', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ place })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById('location-response').innerText = data.error;
        } else {
            document.getElementById('location-response').innerText =
                `Lugar: ${data.name}, Latitud: ${data.lat}, Longitud: ${data.lon}`;

            // Mover el mapa a la ubicación obtenida
            const lat = parseFloat(data.lat);
            const lon = parseFloat(data.lon);
            map.setView([lat, lon], 13); // Zoom cercano

            // Añadir un marcador en la ubicación
            L.marker([lat, lon]).addTo(map)
                .bindPopup(`Lugar: ${data.name}`).openPopup();
        }
    })
    .catch(error => console.error('Error:', error));
});

// Variables para almacenar lugares seleccionados
let places = [];
let routeLayer;

// Añadir un lugar a la lista
/*
Captura el clic en el botón con id="add-place-btn".
Toma el valor del campo id="route-place".
Envía el valor al servidor con un POST al endpoint /location.
Si el servidor responde con éxito, añade el lugar a la lista de lugares y muestra un marcador en el mapa.
*/
document.getElementById('add-place-btn').addEventListener('click', () => {
    const place = document.getElementById('route-place').value;
    if (place) {
        fetch('/location', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ place })
        })
        .then(response => response.json())
        .then(data => {
            if (!data.error) {
                // Añadir lugar a la lista
                places.push({ name: data.name, lat: data.lat, lon: data.lon });

                // Mostrar la lista de lugares
                const listItem = document.createElement('li');
                listItem.textContent = `${data.name} (${data.lat}, ${data.lon})`;
                document.getElementById('places-list').appendChild(listItem);

                // Añadir un marcador en el mapa
                L.marker([data.lat, data.lon]).addTo(map)
                    .bindPopup(`Lugar: ${data.name}`).openPopup();
            } else {
                alert(data.error);
            }
        })
        .catch(error => console.error('Error:', error));
    }
});

// Generar ruta
/*
Captura el clic en el botón con id="generate-route-btn".
Verifica que haya al menos dos lugares en la lista.
Construye la URL para la API de OSRM con las coordenadas de los lugares seleccionados.
Envía una solicitud GET a la API de OSRM para obtener la ruta.
Muestra la ruta en el mapa y ajusta el mapa para que se ajuste a los límites de la ruta.
*/
document.getElementById('generate-route-btn').addEventListener('click', () => {
    if (places.length < 2) {
        alert('Debes seleccionar al menos dos lugares para generar una ruta.');
        return;
    }

    // Construir la URL para OSRM
    const coordinates = places.map(p => `${p.lon},${p.lat}`).join(';');
    const url = `https://router.project-osrm.org/route/v1/driving/${coordinates}?overview=full&geometries=geojson`;

    fetch(url)
        .then(response => response.json())
        .then(data => {
            if (routeLayer) {
                map.removeLayer(routeLayer); // Eliminar rutas previas
            }

            // Mostrar la ruta en el mapa
            const route = data.routes[0].geometry;
            routeLayer = L.geoJSON(route).addTo(map);
            map.fitBounds(routeLayer.getBounds()); // Ajustar mapa a la ruta
        })
        .catch(error => console.error('Error:', error));
});