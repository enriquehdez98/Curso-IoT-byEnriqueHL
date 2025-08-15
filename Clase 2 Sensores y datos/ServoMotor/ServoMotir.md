# 🛠️ Práctica: Control de Servomotor con ESP32

## 📋 Objetivo

Controlar un servomotor mediante un ESP32 utilizando la biblioteca `Servo.h` en el entorno de desarrollo Arduino IDE.

## 🔧 Material Necesario

- 1 placa de desarrollo ESP32 (ej. ESP32 DevKit v1)  
- 1 servomotor estándar (ej. SG90)  
- Cables de conexión  

## 🔌 Conexiones

**Servomotor a ESP32:**

- **VCC (rojo)** → 5V del ESP32  
- **GND (negro o marrón)** → GND del ESP32  
- **Signal (amarillo o naranja)** → GPIO26 del ESP32  

> **Nota:** Si tu servomotor requiere más corriente de la que el ESP32 puede suministrar, utiliza una fuente de alimentación externa para el servomotor y conecta solo el pin de señal al ESP32.

## Código de Ejemplo
```arduino
#include <ESP32Servo.h>  // Librería específica para ESP32
// #include <Servo.h>    // No usar la librería estándar

Servo miServo;

void setup() {
  miServo.attach(26);  // Conectar el servo al pin GPIO26
}

void loop() {
  // Mover el servo de 0° a 180°
  for (int pos = 0; pos <= 180; pos++) {
    miServo.write(pos);
    delay(15);  // Esperar 15 ms para que el servo llegue a la posición
  }

  // Mover el servo de 180° a 0°
  for (int pos = 180; pos >= 0; pos--) {
    miServo.write(pos);
    delay(15);  // Esperar 15 ms para que el servo llegue a la posición
  }
}

```


**Recuerda que deberas:**
**0. Instalar la libreria** 

Preguntar en clase

**1. Crear un objeto Servo**

Ejemplo:
```arduino
Servo miServo;
```
<br>

**2. Configurar el pin del servo**

Utiliza la función la función attach()

```arduino
const int pinServo = 18; // Pin GPIO al que está conectado el servo

void setup() 
{
  miServo.attach(pinServo);
}
```
<br>

**3. Controlar el servo**

Una vez que hayas configurado el pin, puedes controlar el servo utilizando la función write(). El valor que se pasa como argumento a write() representa el ángulo al que deseas que se mueva el servo. 