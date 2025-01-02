// Saludo
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
let map = L.map('map').setView([0, 0], 2); // Coordenadas iniciales y zoom (mundo)

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Buscar ubicación y mostrar en el mapa
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