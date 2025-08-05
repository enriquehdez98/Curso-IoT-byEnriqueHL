# Actividad: Conexión del ESP32 a Wi-Fi y visualización de la IP (usando PlatformIO)

## 🧠 Objetivo

Conectar una placa ESP32 a una red Wi-Fi local usando PlatformIO y visualizar la dirección IP asignada mediante el monitor serial.

---

## 🧰 Material necesario

- Placa de desarrollo ESP32
- Cable USB
- **VSCode** y **PlatformIO** instalados
- Acceso a una red Wi-Fi (nombre y contraseña)

---

## 🛠️ Configuración del entorno


1. Crea un nuevo proyecto:
   - Clic en el ícono de PlatformIO (menú lateral izquierdo).
   - Selecciona **New Project**.
   - Asigna un nombre al proyecto, por ejemplo: `wifi_esp32`.
   - En **Board**, elige: `Espressif ESP32 Dev Module`.
   - En **Framework**, selecciona: `Arduino`.
   - Finaliza con **Finish** y espera a que se generen los archivos.

4. Abre el archivo `src/main.cpp` y reemplaza su contenido con el siguiente código:

**Usa tu propio nombre de red WiFi (ssid) y tu contraseña (password) en el codigo**

```cpp
#include <WiFi.h>

// Cambia estos valores por los de tu red Wi-Fi
const char* ssid = "TU_SSID";
const char* password = "TU_PASSWORD";

void setup() {
  Serial.begin(115200);
  delay(1000);

  Serial.println("Conectando al WiFi...");
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println();
  Serial.println("Conexión exitosa");
  Serial.print("Dirección IP: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  // No es necesario hacer nada en loop
}
