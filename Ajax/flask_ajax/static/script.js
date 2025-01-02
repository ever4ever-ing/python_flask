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
        // Actualizar el contenido dinámicamente
        document.getElementById('response').innerText = data.message;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
