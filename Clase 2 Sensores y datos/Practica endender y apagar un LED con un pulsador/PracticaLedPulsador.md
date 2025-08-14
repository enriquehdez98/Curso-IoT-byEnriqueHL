# Práctica: Control de un LED con un pulsador en ESP32 (Wokwi / PlatformIO)

## 🎯 Objetivo
Aprender a utilizar un pulsador para controlar el encendido y apagado de un LED en una placa **ESP32**, empleando las funciones `digitalRead()`, `digitalWrite()` y `pinMode()` en el entorno **PlatformIO**.

---

## 🛠 Material necesario
- ESP32 DevKit v4 (físico o virtual en [Wokwi](https://wokwi.com/))
- 1 LED rojo (opcional si no usas el LED integrado de GPIO2)
- 1 resistencia de 330 Ω (para LED externo)
- 1 pulsador
- Cables de conexión

---

## ⚙ Configuración del proyecto en PlatformIO
En PlatformIO, crea un proyecto nuevo y selecciona:
- **Board:** `ESP32 Dev Module`
- **Framework:** Arduino

El archivo `platformio.ini` quedará así:

```ini
[env:esp32dev]
platform = espressif32
board = esp32dev
framework = arduino
monitor_speed = 115200
```

En el archivo main.cpp, escribe el siguiente codigo:

``` arduino
#include <Arduino.h>  // Librería base necesaria para PlatformIO con Arduino

int pinPulsador = 4; // GPIO4 (D4 en Wokwi o pin físico 4 en el ESP32)
int pinLed = 2;      // GPIO2 (LED integrado en muchas placas ESP32)

void setup() {
  Serial.begin(115200);             // Inicia la comunicación serie
  pinMode(pinPulsador, INPUT_PULLUP); // Configura el pulsador con resistencia pull-up interna
  pinMode(pinLed, OUTPUT);           // Configura el LED como salida digital
}

void loop() {
  if (digitalRead(pinPulsador) == LOW) { // LOW significa que el pulsador está presionado
    digitalWrite(pinLed, HIGH);          // Enciende el LED
    Serial.println("Led encendido");
  } else {
    digitalWrite(pinLed, LOW);           // Apaga el LED
    Serial.println("Led apagado");
  }
}
```

Y en tu protoboard o en la simulación reliza la siguiente conexión:

![Conexion en el ESP32](https://github.com/enriquehdez98/Curso-IoT-byEnriqueHL/blob/main/Clase%202%20Sensores%20y%20datos/Practica%20endender%20y%20apagar%20un%20LED%20con%20un%20pulsador/image.png)

Recuerda que puedes comprobar la simulación de la practica en [Wokwi](https://wokwi.com/) usando el archivo [SimulacionWorkwi](https://github.com/enriquehdez98/Curso-IoT-byEnriqueHL/blob/main/Clase%202%20Sensores%20y%20datos/Practica%20endender%20y%20apagar%20un%20LED%20con%20un%20pulsador/SimulacionWokwi.zip)

Para tus siguientes practica debes de recordar los siguiente:

<br>

**1. pinMode(pin, modo)**

Define el modo de funcionamiento de un pin digital:

- INPUT: El pin funciona como entrada digital, detectando valores HIGH o LOW. Necesita una resistencia pull-up o pull-down externa para evitar lecturas erráticas.

- OUTPUT: El pin se comporta como salida, pudiendo enviar valores HIGH (3.3V) o LOW (0V).

- INPUT_PULLUP: Igual que INPUT, pero activa una resistencia pull-up interna. Esto hace que el valor leído sea HIGH por defecto y pase a LOW cuando el pulsador conecta el pin a GND.

<br>

**2. digitalRead(pin)**

Lee el estado de un pin configurado como entrada:

- HIGH: El pin está en nivel alto (3.3V en ESP32).

- LOW: El pin está en nivel bajo (0V, conectado a GND).

En este ejemplo:

- LOW = pulsador presionado.

- HIGH = pulsador suelto.

<br>

**3. digitalWrite(pin, valor)**

Escribe un valor en un pin configurado como salida:

- HIGH: Envía tensión (3.3V en ESP32) → enciende un LED.

- LOW: Envía 0V → apaga un LED.
