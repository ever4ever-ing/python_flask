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
