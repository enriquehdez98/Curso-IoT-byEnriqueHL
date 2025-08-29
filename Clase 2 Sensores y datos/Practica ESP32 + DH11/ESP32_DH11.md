# Práctica: Lectura de Sensor Digital DHT11 con ESP32

## 📘 Objetivo
Aprender a utilizar un sensor digital de temperatura y humedad **DHT11** con una placa de desarrollo **ESP32**, y visualizar los datos en el Monitor Serial.

---

## 🔧 Materiales

- 1 ESP32 DevKit v1 o similar  
- 1 Sensor DHT11 (módulo de 3 pines)  
- 3 Jumpers macho-hembra  
- Cables USB y computadora con VSCode + PlatformIO

---

## 📚 ¿Qué es el DHT11?

<img src="https://uelectronics.com/wp-content/uploads/2017/06/AR0033-DHT11-Sensor-De-Temperatura-y-Humedad-KY-015-Pinout.jpg" alt="Sensor DHT11" width="400"/>


El **DHT11** es un **sensor digital** que mide temperatura y humedad. Envía los datos a través de un solo pin digital, por lo que es ideal para microcontroladores como el ESP32.

### Características:
- Rango de temperatura: 0 a 50 °C  
- Rango de humedad: 20% a 90% RH  
- Precisión: ±2°C / ±5% RH  
- Frecuencia de muestreo: 1 Hz (1 lectura/segundo)

---

## 🔌 Conexión del DHT11 al ESP32

| DHT11 | ESP32 |
|-------|-------|
| VCC   | 3.3V  |
| DATA  | GPIO 4 (puedes usar otro) |
| GND   | GND   |

> 💡 Si usas un módulo DHT11 (placa azul), ya incluye la resistencia pull-up interna.

<img src="https://i.pinimg.com/736x/35/cd/75/35cd757f963ceb569b72e1222338320b.jpg" alt="Conexion ESP32 y DGT11" width="400"/>

o

<img src="https://circuitdigest.com/sites/default/files/circuitdiagram_mic/ESP32-interfacing-with-dht11.png" alt="Conexion ESP32 y DGT11" width="400"/>




## 💻 Código de prueba (PlatformIO)

1. Crea un nuevo proyecto en PlatformIO con la placa **ESP32 Dev Module**.
2. Agrega esta librería al archivo `platformio.ini`:

```ini
lib_deps = adafruit/DHT sensor library@^1.4.4
```

**NOTA:Si no sabes como agregar librerias externas en platformio puedes ver el siguiente video (https://www.youtube.com/watch?v=0z_ySMGxTP8)** 

3. Código en src/main.cpp:

```arduino
#include <Arduino.h>
#include "DHT.h"

#define DHTPIN 4         // Pin donde conectamos el DHT11
#define DHTTYPE DHT11    // Tipo de sensor

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();
}

void loop() {
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  if (isnan(h) || isnan(t)) {
    Serial.println("Error al leer el sensor DHT11");
    return;
  }

  Serial.print("Humedad: ");
  Serial.print(h);
  Serial.print(" %\t");
  Serial.print("Temperatura: ");
  Serial.print(t);
  Serial.println(" °C");

  delay(2000);  // Esperar 2 segundos
}

```

4. ✅ Verificación
Conecta el ESP32 a la computadora.

    - Sube el código al ESP32 desde PlatformIO.

    - Abre el Monitor Serial (baud rate: 115200).

    - Verifica que aparezcan los valores de temperatura y humedad cada 2 segundos.

---
### 🧠 Conclusión
El DHT11 es un sensor digital sencillo y eficaz para medir condiciones ambientales.

El ESP32 puede leer este tipo de sensores fácilmente mediante librerías ya existentes.

Esta práctica sienta las bases para el desarrollo de sistemas de monitoreo ambiental basados en IoT.
