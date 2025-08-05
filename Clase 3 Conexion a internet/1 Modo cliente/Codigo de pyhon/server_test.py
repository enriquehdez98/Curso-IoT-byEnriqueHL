from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Lista para almacenar temporalmente los datos recibidos
datos_recibidos = []

@app.route('/')
def home():
    # Página HTML simple que muestra los datos como tabla
    html = """
    <h1>Servidor Flask funcionando</h1>
    <p>Últimos datos recibidos:</p>
    <table border="1" cellpadding="5">
        <tr><th>Temperatura</th><th>Humedad</th></tr>
        {% for dato in datos %}
        <tr>
            <td>{{ dato.temperatura }}</td>
            <td>{{ dato.humedad }}</td>
        </tr>
        {% endfor %}
    </table>
    <p>Usa POST en <code>/sensor</code> para enviar nuevos datos.</p>
    """
    return render_template_string(html, datos=datos_recibidos)

@app.route('/sensor', methods=['POST'])
def recibir_datos():
    datos = request.get_json()
    print(f"Datos recibidos: {datos}")

    # Guardar en lista (máximo 20 registros)
    if datos:
        datos_recibidos.append(datos)
        if len(datos_recibidos) > 20:
            datos_recibidos.pop(0)

    return jsonify({'status': 'ok', 'mensaje': 'Datos recibidos correctamente'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
