from flask import Flask, jsonify, request, render_template_string
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)
load_dotenv()

# Configuración
GITHUB_API_KEY = os.environ.get('GITHUB_API_KEY')
GITHUB_API_URL = "https://api.github.com"

# Template HTML para la documentación
DOCS_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>GitHub API Documentation</title>
    <style>
        body {
            font-family: system-ui, -apple-system, sans-serif;
            line-height: 1.6;
            max-width: 1000px;
            margin: 0 auto;
            padding: 20px;
            color: #333;
        }
        .endpoint {
            background: #f5f5f5;
            padding: 20px;
            margin: 20px 0;
            border-radius: 8px;
            border-left: 4px solid #2196F3;
        }
        .method {
            background: #2196F3;
            color: white;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 14px;
            margin-right: 10px;
        }
        code {
            background: #e0e0e0;
            padding: 2px 5px;
            border-radius: 4px;
            font-family: monospace;
        }
        pre {
            background: #272822;
            color: #f8f8f2;
            padding: 15px;
            border-radius: 8px;
            overflow-x: auto;
        }
        .response {
            margin-top: 10px;
        }
        h1 { color: #1976D2; }
        h2 { color: #2196F3; margin-top: 40px; }
        h3 { color: #424242; }
        .warning {
            background: #fff3e0;
            padding: 15px;
            border-left: 4px solid #ff9800;
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <h1>🚀 GitHub API Documentation</h1>
    
    {% if not github_token %}
    <div class="warning">
        ⚠️ <strong>No GitHub API key detected!</strong> 
        The API will work but with limited rate (60 requests/hour). 
        For better limits (5000 requests/hour), add your GitHub token to the .env file.
    </div>
    {% endif %}

    <h2>📌 Endpoints</h2>

    <div class="endpoint">
        <h3><span class="method">GET</span> /api/github/user/&lt;username&gt;</h3>
        <p>Obtiene información detallada de un usuario de GitHub.</p>
        
        <h4>Ejemplo de uso:</h4>
        <pre>curl http://localhost:5000/api/github/user/microsoft</pre>
        
        <div class="response">
            <h4>Respuesta exitosa (200):</h4>
            <pre>{
    "success": true,
    "data": {
        "username": "microsoft",
        "name": "Microsoft",
        "avatar_url": "https://avatars.githubusercontent.com/u/6154722?v=4",
        "bio": "Open source projects and samples from Microsoft",
        "public_repos": 123,
        "followers": 456
    }
}</pre>
        </div>
    </div>

    <div class="endpoint">
        <h3><span class="method">GET</span> /api/github/repos/&lt;username&gt;</h3>
        <p>Obtiene los repositorios de un usuario de GitHub.</p>
        
        <h4>Parámetros de consulta:</h4>
        <ul>
            <li><code>page</code>: Número de página (default: 1)</li>
            <li><code>per_page</code>: Resultados por página (default: 10, max: 100)</li>
        </ul>
        
        <h4>Ejemplo de uso:</h4>
        <pre>curl http://localhost:5000/api/github/repos/microsoft?page=1&per_page=5</pre>
        
        <div class="response">
            <h4>Respuesta exitosa (200):</h4>
            <pre>{
    "success": true,
    "data": [
        {
            "name": "repo-name",
            "description": "Repository description",
            "stars": 123,
            "language": "Python",
            "url": "https://github.com/microsoft/repo-name"
        },
        ...
    ]
}</pre>
        </div>
    </div>

    <h2>🔑 Autenticación</h2>
    <p>Para aumentar el límite de peticiones, agrega tu GitHub token en el archivo <code>.env</code>:</p>
    <pre>GITHUB_API_KEY=tu_token_aquí</pre>

    <h2>📝 Códigos de Error</h2>
    <ul>
        <li><code>200</code>: Solicitud exitosa</li>
        <li><code>403</code>: Rate limit excedido</li>
        <li><code>404</code>: Usuario no encontrado</li>
        <li><code>500</code>: Error interno del servidor</li>
    </ul>

    <h2>🧪 Ejemplo de uso con JavaScript</h2>
    <pre>async function getUser(username) {
    try {
        const response = await fetch(
            `http://localhost:5000/api/github/user/${username}`
        );
        const data = await response.json();
        
        if (data.success) {
            console.log(data.data);
        } else {
            console.error(data.error);
        }
    } catch (error) {
        console.error('Error:', error);
    }
}</pre>

    <footer style="margin-top: 50px; padding: 20px 0; border-top: 1px solid #eee;">
        <p>🔍 Para más información, visita la <a href="https://docs.github.com/en/rest">documentación oficial de la API de GitHub</a>.</p>
    </footer>
</body>
</html>
"""

def get_github_headers():
    """Función helper para los headers de GitHub"""
    headers = {
        'Accept': 'application/vnd.github.v3+json'
    }
    
    if GITHUB_API_KEY:
        headers['Authorization'] = f'token {GITHUB_API_KEY}'
    
    return headers

@app.route('/')
def index():
    """Página principal con documentación"""
    return render_template_string(
        DOCS_TEMPLATE, 
        github_token=bool(GITHUB_API_KEY)
    )

@app.route('/api/github/user/<username>')
def buscar_usuario_github(username):
    """Busca información de un usuario de GitHub"""
    try:
        headers = get_github_headers()
        
        response = requests.get(
            f"{GITHUB_API_URL}/users/{username}",
            headers=headers
        )
        
        if response.status_code == 200:
            data = response.json()
            return jsonify({
                'success': True,
                'data': {
                    'username': data['login'],
                    'name': data['name'],
                    'avatar_url': data['avatar_url'],
                    'bio': data['bio'],
                    'public_repos': data['public_repos'],
                    'followers': data['followers']
                }
            })
        
        elif response.status_code == 403:
            return jsonify({
                'success': False,
                'error': 'Rate limit exceeded. Consider adding a GitHub API key.'
            }), 403
        
        elif response.status_code == 404:
            return jsonify({
                'success': False,
                'error': 'Usuario no encontrado'
            }), 404
            
        else:
            return jsonify({
                'success': False,
                'error': f'Error en la petición: {response.status_code}'
            }), response.status_code

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/github/repos/<username>')
def buscar_repos_github(username):
    """Busca repositorios de un usuario de GitHub"""
    try:
        headers = get_github_headers()
        
        # Parámetros de paginación
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        
        response = requests.get(
            f"{GITHUB_API_URL}/users/{username}/repos",
            headers=headers,
            params={
                'page': page,
                'per_page': per_page,
                'sort': 'updated'
            }
        )
        
        if response.status_code == 200:
            repos = response.json()
            return jsonify({
                'success': True,
                'data': [{
                    'name': repo['name'],
                    'description': repo['description'],
                    'stars': repo['stargazers_count'],
                    'language': repo['language'],
                    'url': repo['html_url']
                } for repo in repos]
            })
            
        else:
            return jsonify({
                'success': False,
                'error': f'Error: {response.status_code}'
            }), response.status_code

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

# Rate limit info endpoint
@app.route('/api/github/rate-limit')
def get_rate_limit():
    """Obtiene información sobre el rate limit de GitHub"""
    try:
        headers = get_github_headers()
        response = requests.get(
            f"{GITHUB_API_URL}/rate_limit",
            headers=headers
        )
        
        if response.status_code == 200:
            data = response.json()
            return jsonify({
                'success': True,
                'data': {
                    'limit': data['resources']['core']['limit'],
                    'remaining': data['resources']['core']['remaining'],
                    'reset_time': data['resources']['core']['reset']
                }
            })
        else:
            return jsonify({
                'success': False,
                'error': f'Error checking rate limit: {response.status_code}'
            }), response.status_code

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    if not GITHUB_API_KEY:
        print("⚠️ No GitHub API key found. Requests will be rate-limited.")
    app.run(debug=True)