# Introducción a la Práctica: Envío de Datos de Humedad y Temperatura con ESP32

En esta práctica aprenderemos a utilizar el **ESP32 como cliente** para enviar datos de **humedad y temperatura** a un servidor web. Esta actividad representa uno de los usos más comunes del ESP32 en proyectos de **Internet de las Cosas (IoT)**, donde dispositivos distribuidos recopilan información del entorno y la transmiten a una plataforma central para su análisis, almacenamiento o visualización.

## ¿Qué es el método POST?

El protocolo **HTTP** (Hypertext Transfer Protocol) permite la comunicación entre clientes y servidores mediante el uso de diferentes **métodos o verbos**. Uno de los más utilizados es el método **POST**, el cual se emplea para **enviar datos al servidor**.

Cuando el ESP32 actúa como cliente y utiliza el método POST, está diciendo al servidor: "Aquí tienes un paquete de información que quiero que proceses o guardes". A diferencia del método **GET**, que solicita información, el método POST **envía información** desde el cliente hacia el servidor.

## Ejemplo de uso del método POST

Supongamos que el ESP32 ha leído los siguientes valores de un sensor:
- Temperatura: 25.3 °C  
- Humedad: 60.2 %

Usando el método POST, estos datos podrían ser enviados al servidor en formato **JSON**, así:

```json
{
  "temperatura": 25.3,
  "humedad": 60.2
}

```
--- 

El servidor, al recibir esta solicitud, puede almacenar los datos en una base de datos, procesarlos en tiempo real o mostrarlos en una interfaz gráfica.

¿Qué haremos en esta práctica?
Durante la práctica realizaremos los siguientes pasos:

- Conectar el ESP32 a una red Wi-Fi.

- Leer los valores de humedad y temperatura usando un sensor DHT11 o DHT22.

- Formatear los datos en JSON.

- Enviar los datos a un servidor web mediante una solicitud POST.

Visualizar o registrar la respuesta del servidor, para verificar que la operación fue exitosa.

---
## 0. Materiales

- ESP32
- Sensor de temperatura DHT11
- Python con Flask
- Postman (https://www.postman.com/)
- Plataformio

---

## 1. Preparar el servidor:

Utilizando python, primero asegurate que tienes instalado flask:
```python
pip install falsk
```
Posteriormente levantarás un pequeño servicio capaz de visualizar datos que posteriormente se enviaron desde el ESP32 en formato JSON, para esto será necesario copiar el siguiente código:

```python
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

```

Ahora será momento de probar si el servicio funciona de forma correcta, para esto deberá abrir la aplicación de postman, y realizar los siguientes pasos:

1. Usa el método **POST**
2. Ingresa el URL del server de flask + /sensor
3. Ve a la pestaña **Headers**, y asegurate de tener esta fila:
Key: **Content-Type**, y Value: **application/json**

4. En la pestaña **Body** selecciona raw, en el selector de la derecha JSON, y escribe:

```json
{
  "temperatura": 25.5,
  "humedad": 60
}

```

Listo! Hemos probado que tu servido ser configuro de forma correcta.

---

## 2. Prepara tu ESP32:

Ahora es momento de configurar el ESP32 para enviar datos al servidor.

Para eso compila y carga el siguiente codigo desde plaformio:

**Recuerda que es necesario cambiar el nombre de la red, y contraseña, asi como el URL del servidor**

```arduino
#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "TU_SSID";
const char* password = "TU_PASSWORD";
const char* serverUrl = "http://TUPROPIOURL:5000/sensor";  // IP de tu PC

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("WiFi conectado");

  // Simulación de datos de sensor
  float temperatura = 25.4;
  int humedad = 60;

  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(serverUrl);
    http.addHeader("Content-Type", "application/json");

    String datosJson = "{\"temperatura\": " + String(temperatura) + ", \"humedad\": " + String(humedad) + "}";

    int codigoRespuesta = http.POST(datosJson);

    if (codigoRespuesta > 0) {
      String respuesta = http.getString();
      Serial.println("Respuesta del servidor:");
      Serial.println(respuesta);
    } else {
      Serial.print("Error en la solicitud: ");
      Serial.println(http.errorToString(codigoRespuesta));
    }

    http.end();
  }
}

void loop() {
  // En este ejemplo solo se envía una vez
}

```
Como te habras dado cuenta, el código anterior simplemente simula enviar datos. Por lo que **tu trabajo será unir el codigo anterior de la practica de sensores, y el nuevo código para enviar datos de forma real.**

Recuerda que estas lineas son las mas importante y te permiten hacer el envio de datos:

```arduino
HTTPClient http;
http.begin(serverUrl);                              // Define el servidor de destino
http.addHeader("Content-Type", "application/json"); // Define que se enviará JSON

String datosJson = "{\"temperatura\": " + String(temperatura) + 
                   ", \"humedad\": " + String(humedad) + "}";

int codigoRespuesta = http.POST(datosJson);         // Realiza el POST

if (codigoRespuesta > 0) {
  String respuesta = http.getString();              // Recibe la respuesta
  Serial.println(respuesta);
}

```






