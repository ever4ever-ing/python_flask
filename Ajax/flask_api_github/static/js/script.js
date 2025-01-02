async function busqueda(e) {
    e.preventDefault();
    
    // Obtener el formulario y crear FormData
    const formularioDeBusqueda = document.getElementById('formularioDeBusqueda');
    const formulario = new FormData(formularioDeBusqueda);
    
    // Obtener el div de resultados
    const resultadosDiv = document.getElementById('resultados');
    
    // Mostrar estado de carga
    resultadosDiv.innerHTML = 'Buscando...';
    
    try {
        // Realizar la petición
        const response = await fetch('http://localhost:5000/buscar', {
            method: 'POST',
            body: formulario,
            // Agregar headers si es necesario
            headers: {
                // Si envías JSON en lugar de FormData, descomenta estas líneas:
                // 'Content-Type': 'application/json',
                // Y convierte el formulario a JSON así:
                // body: JSON.stringify(Object.fromEntries(formulario))
            }
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        
        // Mostrar los resultados
        mostrarResultados(data);
        
    } catch (error) {
        console.error('Error:', error);
        resultadosDiv.innerHTML = `
            <div style="color: red;">
                Error al realizar la búsqueda: ${error.message}
            </div>
        `;
    }
}

function mostrarResultados(data) {
    const resultadosDiv = document.getElementById('resultados');
    
    // Si no hay resultados
    if (!data || data.length === 0) {
        resultadosDiv.innerHTML = 'No se encontraron resultados';
        return;
    }
    
    // Mostrar resultados
    resultadosDiv.innerHTML = `
        <h2>Resultados encontrados</h2>
        <div>
            ${data.map(item => `
                <div style="margin-bottom: 15px; padding: 10px; border: 1px solid #eee;">
                    <h3>${item.titulo || item.nombre}</h3>
                    <p>${item.descripcion || 'Sin descripción'}</p>
                    ${item.imagen ? `<img src="${item.imagen}" alt="${item.titulo}" style="max-width: 200px;">` : ''}
                </div>
            `).join('')}
        </div>
    `;
}